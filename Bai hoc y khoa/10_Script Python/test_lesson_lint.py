"""Regression tests for lesson_lint.py, specialties.py and release_lesson.py (mọi chuyên khoa)."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import lesson_lint as LL
import lesson_manifest as LM
import release_lesson
import specialties

CHAIN = "> 🔄 **Chuỗi cơ chế:** thiếu surfactant → xẹp phế nang → shunt → giảm oxy máu\n"


def make_lesson(root: Path, folder: str, specialty: str, lesson_id: str, body: str, **extra) -> Path:
    lesson_dir = root / folder
    lesson_dir.mkdir(parents=True)
    name = f"{lesson_id}_Bai_thu_2026-10-19_RELEASE_v1.md"
    (lesson_dir / name).write_text(body, encoding="utf-8")
    (lesson_dir / "cards.py").write_text("cards_data = []", encoding="utf-8")
    manifest = {"id": lesson_id, "specialty": specialty, "profile": "foundation", "lesson": name,
                "deck": {"deck_id": 1, "deck_name": "x", "basename": Path(name).stem, "cards_source": "cards.py"}}
    manifest.update(extra)
    (lesson_dir / "lesson.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
    return lesson_dir


def codes(lesson_dir: Path) -> list[str]:
    return [i.code for i in LL.lint_lesson(LM.load(lesson_dir))]


class SpecialtyRegistry(unittest.TestCase):
    def test_lesson_id_from_folder_per_specialty(self):
        self.assertEqual(specialties.get("nhi").lesson_id_from_folder("PED-13_Suy_ho_hap"), "PED-13")
        self.assertEqual(specialties.get("noi").lesson_id_from_folder("IM-07b_Suy_ho_hap_cap"), "IM-07b")
        self.assertEqual(specialties.get("art").lesson_id_from_folder("44_Semen_Analysis"), "ART-44")
        self.assertEqual(specialties.get("vi_sinh").lesson_id_from_folder("V4_HPV"), "MIC-4")
        self.assertIsNone(specialties.get("noi").lesson_id_from_folder("IM_khong_ma"))

    def test_deck_name_allows_group_level_but_requires_root_and_id(self):
        art = specialties.get("art")
        self.assertIsNone(art.deck_name_error("2. Y Khoa - Sản Phụ Khoa & ART::Hỗ Trợ Sinh Sản (ART)::ART-44 Tinh dịch đồ", "ART-44"))
        self.assertIsNotNone(art.deck_name_error("ART::Semen_Analysis::2026-07-13"))
        self.assertIsNotNone(art.deck_name_error("2. Y Khoa - Sản Phụ Khoa & ART::Hỗ Trợ Sinh Sản (ART)::Tinh dịch đồ"))

    def test_specialty_found_from_path(self):
        p = specialties.LESSONS_ROOT / "11_Noi khoa" / "02_Tim_mach" / "IM-22_Suy_tim" / "x.md"
        self.assertEqual(specialties.for_path(p).key, "noi")


class FormatAndChains(unittest.TestCase):
    def test_tab_from_python_text_escape_and_latex_are_flagged_outside_code_fences(self):
        body = "# Bài\n\n\text{ANC} = WBC × %\n\n$$ANC$$\n\n```text\n\tcây ├── nhánh\n$$ trong fence $$\n```\n" + CHAIN * 3
        with tempfile.TemporaryDirectory() as t:
            found = LL.check_format((make_lesson(Path(t), "12_Nhi khoa/PED-98_Thu", "nhi", "PED-98", body)
                                     / "PED-98_Bai_thu_2026-10-19_RELEASE_v1.md").read_text(encoding="utf-8"))
        lines = {i.card_id for i in found}
        self.assertIn("dòng 3", lines)        # \t (tab) + "ext{" ngoài fence
        self.assertIn("dòng 5", lines)        # $$
        self.assertFalse({"dòng 8", "dòng 9"} & lines)  # trong fence không tính
        self.assertIn("F_TAB_INDENT", {i.code for i in found})

    def test_indented_paragraph_after_blank_line_is_code_block_but_nested_list_is_not(self):
        bad = LL.check_format("Đoạn văn.\n\n    thụt vào thành code\n")
        ok = LL.check_format("- mục cha\n\n    tiếp nối mục cha\n")
        self.assertIn("F_INDENTED_CODE", [i.code for i in bad])
        self.assertEqual([i.code for i in ok], [])

    def test_chain_blockquote_count_against_profile(self):
        import depth_check
        cfg = depth_check.get_depth_config("foundation")  # cần ≥3
        self.assertTrue(LL.check_chains(CHAIN * 2 + "A → B → C → D (không phải blockquote)\n", cfg))
        self.assertEqual(LL.check_chains(CHAIN * 3, cfg), [])


class Images(unittest.TestCase):
    def test_image_rules(self):
        from PIL import Image
        with tempfile.TemporaryDirectory() as t:
            d = make_lesson(Path(t), "12_Nhi khoa/PED-98_Thu", "nhi", "PED-98", "x")
            (d / "outputs/figures").mkdir(parents=True)
            Image.new("RGB", (1600, 100)).save(d / "outputs/figures/PED98_fig1_xquang.jpg")
            Image.new("RGB", (100, 100)).save(d / "outputs/figures/anh.jpg")
            text = ("![X-quang](outputs/figures/PED98_fig1_xquang.jpg)\n![](outputs/figures/anh.jpg)\n"
                    "![web](https://example.org/a.jpg)\n")
            found = {i.code for i in LL.check_images(text, LM.load(d))}
        self.assertTrue({"I_SIZE", "I_NAME", "I_ALT", "I_REMOTE"} <= found)


class Labels(unittest.TestCase):
    def _ncbi_lesson(self, t: Path, line: str) -> Path:
        d = make_lesson(t, "12_Nhi khoa/PED-98_Thu", "nhi", "PED-98", f"# Bài\n{line}\n")
        (d / "ncbi_fetch.json").write_text(json.dumps({
            "111111": {"publication_types": ["Journal Article"]},
            "222222": {"publication_types": ["Practice Guideline"]}}), encoding="utf-8")
        (d / "abstract_match.jsonl").write_text(json.dumps({"pmid": "222222", "match": True}) + "\n", encoding="utf-8")
        (d / "full_verify_table.md").write_text("| claim | 111111 |", encoding="utf-8")
        return d

    def _codes(self, line: str) -> set:
        with tempfile.TemporaryDirectory() as t:
            d = self._ncbi_lesson(Path(t), line)
            return {i.code for i in LL.check_labels(LM.load(d).lesson_path.read_text(encoding="utf-8"), LM.load(d))}

    def test_label_needs_matching_artifact_in_ncbi_mode(self):
        self.assertEqual(self._codes("Liều X (PMID: 222222) [GUIDELINE VERIFIED]"), set())
        self.assertEqual(self._codes("Tỷ lệ 30% (PMID: 111111) [DATA VERIFIED]"), set())
        self.assertIn("V_NOT_FETCHED", self._codes("Tỷ lệ 30% (PMID: 999999) [DATA VERIFIED]"))
        self.assertIn("V_NOT_GUIDELINE", self._codes("Khuyến cáo (PMID: 111111) [GUIDELINE VERIFIED]"))
        self.assertIn("V_NO_ABSTRACT_MATCH", self._codes("Kết luận (PMID: 111111) [ABSTRACT VERIFIED]"))
        self.assertIn("V_NO_PMID", self._codes("Kết luận không nguồn [ABSTRACT VERIFIED]"))
        self.assertIn("V_BANNED_LABEL", self._codes("Số liệu (PMID: 111111) [FULL VERIFIED]"))

    def test_evidence_bundle_specialty_leaves_claims_to_build_pipeline(self):
        with tempfile.TemporaryDirectory() as t:
            d = make_lesson(Path(t), "11_Noi khoa/02_Tim_mach/IM-98_Thu", "noi", "IM-98",
                            "Số liệu (PMID: 999999) [DATA VERIFIED]\nCũ [TEXTBOOK]\n")
            found = {i.code for i in LL.check_labels(LM.load(d).lesson_path.read_text(encoding="utf-8"), LM.load(d))}
        self.assertEqual(found, {"V_BANNED_LABEL"})


class ManifestAndModes(unittest.TestCase):
    def test_profile_must_match_brief_contract_and_mode_decides_severity(self):
        with tempfile.TemporaryDirectory() as t:
            d = make_lesson(Path(t), "12_Nhi khoa/PED-98_Thu", "nhi", "PED-98", "# ngắn\n", brief="brief.md")
            (d / "brief.md").write_text('## 0. Lesson profile & release contract\n\n```json\n{"profile": "disease"}\n```\n',
                                        encoding="utf-8")
            self.assertIn("M_PROFILE", codes(d))
            _, release = LL.run(d, "release", quiet=True)
            _, hotfix = LL.run(d, "hotfix", quiet=True)
        self.assertTrue(release and all(i.severity == "BLOCK" for i in release))
        self.assertTrue(all(i.severity == "DEBT" for i in hotfix))

    def test_lesson_id_must_match_folder_and_specialty(self):
        with tempfile.TemporaryDirectory() as t:
            d = make_lesson(Path(t), "12_Nhi khoa/PED-98_Thu", "nhi", "PED-97", "x")
            self.assertTrue(any("khác mã suy từ folder" in e for e in LM.validate(LM.load(d))))

    def test_evidence_bundle_release_requires_bundle_arguments(self):
        with tempfile.TemporaryDirectory() as t:
            d = make_lesson(Path(t), "11_Noi khoa/02_Tim_mach/IM-98_Thu", "noi", "IM-98", "x")
            with patch.object(release_lesson.lesson_lint, "run", return_value=(0, [])):
                self.assertEqual(release_lesson.release(d, "release", False, None, None), 2)
            steps = json.loads((d / "outputs/verification/IM-98_Bai_thu_2026-10-19_RELEASE_v1/release.json")
                               .read_text(encoding="utf-8"))["steps"]
        self.assertEqual(steps[-1], {"step": "evidence_pipeline", "exit_code": 2, "status": "BLOCK"})


if __name__ == "__main__":
    unittest.main()
