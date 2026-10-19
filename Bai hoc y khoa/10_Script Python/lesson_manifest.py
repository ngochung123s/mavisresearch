# -*- coding: utf-8 -*-
"""lesson_manifest.py — đọc + kiểm `lesson.json` (manifest duy nhất của 1 bài học, mọi chuyên khoa).

    {
      "id": "PED-13", "specialty": "nhi", "profile": "disease",
      "lesson": "PED-13_..._RELEASE_v1.md", "brief": "PED-13_RESEARCH_BRIEF.md", "barem": "PED-13_..._PEDYTB.md",
      "deck": {
        "deck_id": 4631985485563, "deck_name": "Nhi khoa Y6::PED-13: …", "basename": "PED-13_…_MASTER_v2",
        "required_sections": ["B0", …], "cards_source": "ped13_cards_data.py",
        "legacy_anki_decks": [], "media_dir": "outputs/figures"
      }
    }

`brief`, `barem`, `legacy_anki_decks`, `media_dir`, `models` là tùy chọn. Xem RULES_LESSON_APKG.md §3.
"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import specialties  # noqa: E402

MANIFEST_NAME = "lesson.json"
PROFILES = ("disease", "foundation", "pharmacology")


class ManifestError(ValueError):
    pass


@dataclass
class Manifest:
    lesson_dir: Path
    id: str
    specialty: specialties.Specialty
    profile: str
    lesson: str | None
    brief: str | None
    barem: str | None
    deck: dict = field(default_factory=dict)

    # ---- đường dẫn suy ra
    @property
    def lesson_path(self) -> Path | None:
        return self.lesson_dir / self.lesson if self.lesson else None

    @property
    def basename(self) -> str:
        return self.deck["basename"]

    @property
    def artifact_dir(self) -> Path:
        return (self.lesson_dir / self.specialty.artifact_dir).resolve()

    @property
    def apkg_path(self) -> Path:
        return self.artifact_dir / f"{self.basename}.apkg"

    @property
    def cards_source_path(self) -> Path:
        return self.lesson_dir / self.deck["cards_source"]

    @property
    def cards_json_path(self) -> Path:
        """cards.v2.json: chính là nguồn nếu cards_source là JSON; nếu nguồn là .py thì builder sinh ra."""
        if self.cards_source_path.suffix == ".json":
            return self.cards_source_path
        return self.artifact_dir / f"{self.basename}.cards.v2.json"

    @property
    def lock_path(self) -> Path:
        return self.lesson_dir / "anki_lock.json"

    @property
    def verify_dir(self) -> Path:
        return self.lesson_dir / "outputs" / "verification" / self.basename

    @property
    def media_dir(self) -> Path:
        return self.lesson_dir / self.deck.get("media_dir", "outputs/figures")

    def load_raw_cards(self) -> list[dict]:
        src = self.cards_source_path
        if src.suffix == ".json":
            data = json.loads(src.read_text(encoding="utf-8"))
            return data["cards"] if isinstance(data, dict) else data
        loader = importlib.util.spec_from_file_location(src.stem, src)
        module = importlib.util.module_from_spec(loader)
        loader.loader.exec_module(module)
        return module.cards_data

    def lint_spec(self) -> dict:
        """Spec cho card_lint.lint_cards."""
        return {**self.deck, "specialty": self.specialty.key, "id": self.id}


def load(lesson_dir: Path) -> Manifest:
    lesson_dir = Path(lesson_dir).resolve()
    path = lesson_dir / MANIFEST_NAME
    if not path.exists():
        raise ManifestError(f"thiếu {MANIFEST_NAME} trong {lesson_dir}")
    data = json.loads(path.read_text(encoding="utf-8"))
    missing = [k for k in ("id", "specialty", "profile", "deck") if k not in data]
    if missing:
        raise ManifestError(f"{path.name}: thiếu trường {missing}")
    deck_missing = [k for k in ("deck_id", "deck_name", "basename", "cards_source") if k not in data["deck"]]
    if deck_missing:
        raise ManifestError(f"{path.name}: deck thiếu trường {deck_missing}")
    return Manifest(lesson_dir=lesson_dir, id=data["id"], specialty=specialties.get(data["specialty"]),
                    profile=data["profile"], lesson=data.get("lesson"), brief=data.get("brief"),
                    barem=data.get("barem"), deck=data["deck"])


def validate(m: Manifest) -> list[str]:
    """Lỗi cấu hình manifest (rỗng = hợp lệ)."""
    errors = []
    if not re.fullmatch(m.specialty.id_re, m.id):
        errors.append(f"mã bài {m.id!r} không đúng dạng {m.specialty.id_prefix}-<số>")
    folder_id = m.specialty.lesson_id_from_folder(m.lesson_dir.name)
    if folder_id and folder_id != m.id:
        errors.append(f"mã bài {m.id} khác mã suy từ folder ({folder_id})")
    if m.specialty.folder not in m.lesson_dir.parts:
        errors.append(f"folder bài không nằm trong {m.specialty.folder}/")
    if m.profile not in PROFILES:
        errors.append(f"profile {m.profile!r} không thuộc {PROFILES}")
    for label, rel in (("lesson", m.lesson), ("brief", m.brief), ("barem", m.barem)):
        if rel and not (m.lesson_dir / rel).exists():
            errors.append(f"{label}: không thấy file {rel}")
    if not m.cards_source_path.exists():
        errors.append(f"cards_source: không thấy {m.deck['cards_source']}")
    if m.specialty.evidence_mode == "evidence_bundle" and m.lesson and m.basename != Path(m.lesson).stem:
        errors.append("chuyên khoa evidence_bundle: deck.basename phải trùng tên file bài (build_pipeline dùng lesson.stem)")
    return errors
