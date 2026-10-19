# -*- coding: utf-8 -*-
"""specialties.py — đọc registry `specialties.json`: chuyên khoa, mã bài, tên deck, chế độ evidence.

Một nguồn duy nhất cho mọi công cụ build bài/APKG (lesson_lint, card_lint, deck_builder, anki_sync,
release_lesson, debt_ledger). Thêm chuyên khoa mới = thêm 1 mục trong specialties.json.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

REGISTRY_PATH = Path(__file__).resolve().parent / "specialties.json"
LESSONS_ROOT = Path(__file__).resolve().parent.parent  # "Bai hoc y khoa"
EVIDENCE_MODES = {"ncbi_artifacts", "evidence_bundle"}
VN_DIACRITIC_RE = re.compile(
    r"[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]", re.I
)


@dataclass(frozen=True)
class Specialty:
    key: str
    name: str
    folder: str
    id_prefix: str
    id_from: str
    deck_root: str
    deck_example: str
    evidence_mode: str
    artifact_dir: str
    curriculum: str
    post_release: tuple[str, ...]
    models: tuple = ()  # (("basic", {...}), ("cloze", {...})) — notetype riêng của chuyên khoa (rỗng = YKhoa_Master_*)

    @property
    def model_overrides(self) -> dict:
        return dict(self.models)

    @property
    def id_re(self) -> str:
        return rf"{re.escape(self.id_prefix)}-\d+[a-z]?"

    @property
    def archive_root(self) -> str:
        return f"{self.deck_root}::_Archive"

    def lesson_id_from_folder(self, folder_name: str) -> str | None:
        """Mã bài suy từ tên folder: `PED-13_…` / `IM-07b_…` hoặc `44_…` / `V4_…` → `ART-44` / `MIC-4`."""
        m = re.match(rf"({self.id_re})(?:_|$)", folder_name)
        if m:
            return m.group(1)
        if self.id_from == "folder_number":
            m = re.match(r"V?(\d+)_", folder_name)
            if m:
                return f"{self.id_prefix}-{m.group(1)}"
        return None

    def deck_name_error(self, deck_name: str, lesson_id: str | None = None) -> str | None:
        """None nếu tên deck hợp lệ: `<deck_root>::[nhóm::]*<ID>[:] <Tên có dấu>[ (EBM Update)]`."""
        pattern = rf"^{re.escape(self.deck_root)}::(?:[^:]+::)*({self.id_re}):? (\S.*?)( \(EBM Update\))?$"
        m = re.match(pattern, deck_name or "")
        if not m:
            return f"phải có dạng `{self.deck_root}::[nhóm::]<{self.id_prefix}-xx> <Tên>` (ví dụ: {self.deck_example})"
        if lesson_id and m.group(1) != lesson_id:
            return f"mã bài trong tên deck ({m.group(1)}) khác mã bài ({lesson_id})"
        if not VN_DIACRITIC_RE.search(m.group(2)):
            return "tên bài trong deck phải viết tiếng Việt có dấu"
        return None


@lru_cache(maxsize=1)
def load() -> dict[str, Specialty]:
    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    out = {}
    for item in data["specialties"]:
        item = {k: v for k, v in item.items() if not k.startswith("_")}
        item["post_release"] = tuple(item.get("post_release", []))
        item["models"] = tuple((k, v) for k, v in item.get("models", {}).items() if not k.startswith("_"))
        spec = Specialty(**item)
        if spec.evidence_mode not in EVIDENCE_MODES:
            raise ValueError(f"{spec.key}: evidence_mode không hợp lệ {spec.evidence_mode!r}")
        out[spec.key] = spec
    return out


def get(key: str) -> Specialty:
    try:
        return load()[key]
    except KeyError:
        raise KeyError(f"chuyên khoa không có trong specialties.json: {key!r} (có: {', '.join(load())})") from None


def for_path(path: Path) -> Specialty | None:
    """Chuyên khoa chứa `path` (theo folder cấp 1 dưới `Bai hoc y khoa`)."""
    parts = Path(path).resolve().parts
    for spec in load().values():
        if spec.folder in parts:
            return spec
    return None


def for_deck_name(deck_name: str) -> list[Specialty]:
    return [s for s in load().values() if (deck_name or "").startswith(s.deck_root + "::")]
