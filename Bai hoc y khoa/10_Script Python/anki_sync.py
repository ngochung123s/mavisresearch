# -*- coding: utf-8 -*-
"""anki_sync.py — đồng bộ bộ thẻ của 1 bài (mọi chuyên khoa) vào Anki qua AnkiConnect, KHÔNG mất lịch sử ôn.

Quy tắc (RULES_LESSON_APKG.md §6):
- Note đã khớp (theo `anki_lock.json`) → cập nhật field tại chỗ, giữ lịch sử ôn.
- Thẻ mới → addNote.
- Note còn trong deck nhưng không còn trong bộ thẻ → chuyển sang `<deck_root>::_Archive::<Mã bài>`,
  suspend, tag `lesson_archived`. KHÔNG xóa note của người học.
- Deck cũ (tên lệch chuẩn) sau khi rỗng thì bị xóa.
- Ảnh được thẻ tham chiếu (`<img src>`) được đưa vào thư mục media của Anki (storeMediaFile).
- Cuối cùng đối soát: số note trong deck == số thẻ input, mọi field khớp, mọi ảnh có trong media Anki.
"""
from __future__ import annotations

import difflib
import json
import sqlite3
import tempfile
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

from card_lint import card_kind, norm_key

ANKI_URL = "http://127.0.0.1:8765"
ARCHIVE_TAG = "lesson_archived"
FIELD_ALIASES = {
    "front": ("Front", "Question"),
    "back": ("Back", "Answer"),
    "text": ("Text",),
    "extra": ("Extra",),
    "category": ("Category",),
    "badge": ("Badge",),
    "badge_class": ("BadgeClass",),
}
FUZZY_MIN = 0.90


class AnkiError(RuntimeError):
    pass


def ac(action: str, **params):
    """Gọi AnkiConnect. Chỉ retry khi chắc chắn lệnh CHƯA được thực thi (Anki tạm đóng collection
    khi backup/sync, hoặc cổng chưa mở). Lỗi giữa chừng (timeout/reset) thì raise — chạy lại sync
    vẫn an toàn vì bootstrap_lock ghép lại note theo nội dung."""
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    for attempt in range(30):
        try:
            with urllib.request.urlopen(urllib.request.Request(ANKI_URL, payload), timeout=900) as resp:
                out = json.loads(resp.read())
        except urllib.error.URLError as exc:
            if isinstance(exc.reason, ConnectionRefusedError) and attempt < 29:
                time.sleep(10)
                continue
            raise
        if out.get("error") and "collection is not available" in str(out["error"]) and attempt < 29:
            time.sleep(10)
            continue
        if out.get("error"):
            raise AnkiError(f"{action}: {out['error']}")
        return out["result"]
    raise AnkiError(f"{action}: Anki không phản hồi")


def _search_escape(name: str) -> str:
    return name.replace("\\", "\\\\").replace('"', '\\"').replace("*", "\\*").replace("_", "\\_")


def notes_in_deck(deck: str, include_children: bool = False) -> list[int]:
    if deck not in ac("deckNames"):
        return []
    card_ids = ac("findCards", query=f'deck:"{_search_escape(deck)}"')
    if not card_ids:
        return []
    infos = ac("cardsInfo", cards=card_ids)
    keep = {c["note"] for c in infos if c["deckName"] == deck or (include_children and c["deckName"].startswith(deck + "::"))}
    return sorted(keep)


def anki_guids(deck: str) -> dict[int, str]:
    """Lấy GUID note của 1 deck bằng exportPackage (collection đang mở nên không đọc SQLite trực tiếp được)."""
    if deck not in ac("deckNames"):
        return {}
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "export.apkg"
        ac("exportPackage", deck=deck, path=str(out), includeSched=False)
        with zipfile.ZipFile(out) as zf:
            names = zf.namelist()
            db = next(n for n in ("collection.anki21", "collection.anki2") if n in names)
            zf.extract(db, tmp)
        con = sqlite3.connect(Path(tmp) / db)
        try:
            return {nid: guid for nid, guid in con.execute("select id, guid from notes")}
        finally:
            con.close()


def field_map(card: dict, anki_fields: list[str]) -> dict[str, str]:
    """Ánh xạ field chuẩn của thẻ → tên field của notetype trong Anki."""
    mapped = {}
    for key, aliases in FIELD_ALIASES.items():
        if key not in card:
            continue
        target = next((a for a in aliases if a in anki_fields), None)
        if target:
            mapped[target] = card[key] or ""
    return mapped


def _prompt(card: dict) -> str:
    return norm_key(card.get("front") or card.get("text") or "")


def _anki_prompt(info: dict) -> str:
    fields = info["fields"]
    for key in ("Front", "Question", "Text"):
        if key in fields:
            return norm_key(fields[key]["value"])
    return norm_key(next(iter(fields.values()))["value"])


def _is_cloze_model(model_name: str, cache: dict) -> bool:
    if model_name not in cache:
        cache[model_name] = "Text" in ac("modelFieldNames", modelName=model_name) and \
            any("{{cloze:" in t["Front"] for t in ac("modelTemplates", modelName=model_name).values())
    return cache[model_name]


def bootstrap_lock(cards: list[dict], candidate_infos: list[dict], lock: dict) -> dict:
    """Ghép thẻ chưa có trong lock với note Anki hiện có: legacy_note_id → khớp nguyên văn → fuzzy ≥ 0.90."""
    by_id = {i["noteId"]: i for i in candidate_infos}
    used = {v["note_id"] for v in lock.values() if v.get("note_id") in by_id}
    model_cache: dict = {}

    def kind_ok(card, info):
        return (card_kind(card) == "cloze") == _is_cloze_model(info["modelName"], model_cache)

    pending = [c for c in cards if c["id"] not in lock or lock[c["id"]].get("note_id") not in by_id]
    for card in list(pending):
        nid = card.get("legacy_note_id")
        if nid and int(nid) in by_id and int(nid) not in used and kind_ok(card, by_id[int(nid)]):
            lock[card["id"]] = {"note_id": int(nid)}
            used.add(int(nid))
            pending.remove(card)
    exact: dict[str, list[int]] = {}
    for nid, info in by_id.items():
        exact.setdefault(_anki_prompt(info), []).append(nid)
    for card in list(pending):
        for nid in exact.get(_prompt(card), []):
            if nid not in used and kind_ok(card, by_id[nid]):
                lock[card["id"]] = {"note_id": nid}
                used.add(nid)
                pending.remove(card)
                break
    for card in pending:
        best, score = None, 0.0
        for nid, info in by_id.items():
            if nid in used or not kind_ok(card, info):
                continue
            ratio = difflib.SequenceMatcher(None, _prompt(card), _anki_prompt(info)).ratio()
            if ratio > score:
                best, score = nid, ratio
        if best is not None and score >= FUZZY_MIN:
            lock[card["id"]] = {"note_id": best}
            used.add(best)
    return lock


def ensure_model(model: dict) -> None:
    if model["name"] in ac("modelNames"):
        return
    ac("createModel", modelName=model["name"], inOrderFields=model["fields"], css=model["css"],
       isCloze=model["is_cloze"],
       cardTemplates=[{"Name": model["template_name"], "Front": model["qfmt"], "Back": model["afmt"]}])


def sync(code: str, specialty, deck_name: str, cards: list[dict], models: dict[str, dict], lock: dict,
         legacy_decks: list[str] | None = None, media: list[Path] | None = None, log=print) -> dict:
    """Đồng bộ `cards` (field đã escape, đúng nội dung APKG) vào deck. Trả về báo cáo, cập nhật `lock` tại chỗ."""
    archive_deck = f"{specialty.archive_root}::{code}"
    source_decks = [deck_name] + [d for d in (legacy_decks or []) if d != deck_name]
    candidate_ids = sorted({nid for d in source_decks for nid in notes_in_deck(d)})
    infos = ac("notesInfo", notes=candidate_ids) if candidate_ids else []
    bootstrap_lock(cards, infos, lock)
    info_by_id = {i["noteId"]: i for i in infos}
    guids: dict[int, str] = {}
    for deck in source_decks:
        guids.update(anki_guids(deck))

    ac("createDeck", deck=deck_name)
    for path in media or []:
        ac("storeMediaFile", filename=path.name, path=str(path))
    for m in models.values():
        ensure_model(m)

    report = {"updated": 0, "unchanged": 0, "added": 0, "archived": 0, "moved": 0, "media": len(media or [])}
    kept: set[int] = set()
    updates, tag_groups = [], {}
    for card in cards:
        entry = lock.get(card["id"], {})
        info = info_by_id.get(entry.get("note_id"))
        if info:
            nid = info["noteId"]
            new_fields = field_map(card, list(info["fields"]))
            changed = {k: v for k, v in new_fields.items() if info["fields"][k]["value"] != v}
            if changed:
                updates.append({"action": "updateNoteFields", "params": {"note": {"id": nid, "fields": changed}}})
            if card.get("tags"):
                tag_groups.setdefault(" ".join(card["tags"]), []).append(nid)
            entry["guid"] = guids.get(nid, entry.get("guid"))
            lock[card["id"]] = entry
            kept.add(nid)
    report["updated"], report["unchanged"] = len(updates), len(kept) - len(updates)
    for start in range(0, len(updates), 50):
        for res in ac("multi", actions=updates[start:start + 50]):
            if isinstance(res, dict) and res.get("error"):
                raise AnkiError(f"updateNoteFields: {res['error']}")
    for tags, nids in tag_groups.items():
        ac("addTags", notes=nids, tags=tags)
    # thẻ mới
    for card in cards:
        if lock.get(card["id"], {}).get("note_id") in kept:
            continue
        model = models["cloze" if card_kind(card) == "cloze" else "basic"]
        nid = ac("addNote", note={"deckName": deck_name, "modelName": model["name"],
                                  "fields": field_map(card, model["fields"]),
                                  "tags": card.get("tags") or [code],
                                  "options": {"allowDuplicate": True}})
        lock[card["id"]] = {"note_id": nid, "guid": None}
        kept.add(nid)
        report["added"] += 1
    # chuyển note giữ lại về deck chuẩn
    kept_cards = [c for i in ac("notesInfo", notes=sorted(kept)) for c in i["cards"]]
    misplaced = [c["cardId"] for c in ac("cardsInfo", cards=kept_cards) if c["deckName"] != deck_name]
    if misplaced:
        ac("changeDeck", cards=misplaced, deck=deck_name)
        report["moved"] = len(misplaced)
    # lưu trữ note không còn dùng
    orphans = [nid for nid in candidate_ids if nid not in kept]
    if orphans:
        orphan_cards = [c for i in ac("notesInfo", notes=orphans) for c in i["cards"]]
        ac("createDeck", deck=archive_deck)
        ac("changeDeck", cards=orphan_cards, deck=archive_deck)
        ac("suspend", cards=orphan_cards)
        ac("addTags", notes=orphans, tags=ARCHIVE_TAG)
        report["archived"] = len(orphans)
    # xóa deck cũ đã rỗng
    for deck in source_decks[1:]:
        if deck in ac("deckNames") and not ac("findCards", query=f'deck:"{_search_escape(deck)}"'):
            ac("deleteDecks", decks=[deck], cardsToo=True)
            log(f"  [ANKI] đã xóa deck cũ rỗng: {deck}")
    # GUID cho note mới (sau khi tạo mới có)
    fresh = anki_guids(deck_name)
    for entry in lock.values():
        if entry.get("note_id") in fresh:
            entry["guid"] = fresh[entry["note_id"]]

    # đối soát
    final_ids = notes_in_deck(deck_name)
    if sorted(final_ids) != sorted(kept) or len(final_ids) != len(cards):
        raise AnkiError(f"đối soát lệch: deck có {len(final_ids)} note, input {len(cards)} thẻ")
    final = {i["noteId"]: i for i in ac("notesInfo", notes=final_ids)}
    for card in cards:
        info = final[lock[card["id"]]["note_id"]]
        for key, value in field_map(card, list(info["fields"])).items():
            if info["fields"][key]["value"] != value:
                raise AnkiError(f"field lệch sau sync: {card['id']} / {key}")
    if missing := [p.name for p in media or [] if not ac("retrieveMediaFile", filename=p.name)]:
        raise AnkiError(f"ảnh chưa có trong media Anki: {missing}")
    report["deck_notes"] = len(final_ids)
    return report
