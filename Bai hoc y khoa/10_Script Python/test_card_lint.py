"""Regression tests for card_lint.py + deck_builder.py (mọi chuyên khoa)."""
import json
import sqlite3
import tempfile
import textwrap
import unittest
import zipfile
from pathlib import Path

import card_lint as L
import deck_builder as B

GOOD_BACK = ('<b>🎯 Trả lời cốt lõi:</b><br><span style="color:#ff6b6b"><b>Sốt cao</b></span>'
             '<br><br><b>💡 Giải thích của AI:</b><br>Giải thích cơ chế.')
GOOD_FRONT = 'Triệu chứng <span style="color:#74c0fc"><b>viêm màng não</b></span> là gì?'


def basic(cid="X-1", **kw):
    card = {"id": cid, "type": "basic", "section": "B1", "front": GOOD_FRONT, "back": GOOD_BACK,
            "extra": "📖 Nguồn: Nelson 21st"}
    card.update(kw)
    return card


def codes(cards, spec=None):
    return [i.code for i in L.lint_cards(cards, spec)]


class TechnicalGates(unittest.TestCase):
    def test_half_escaped_tags_block(self):
        # Lỗi PED-46: `&lt;b>` hiển thị tag thô; bộ linter cũ chỉ tìm `&lt;b&gt;` nên bỏ lọt.
        card = basic(back="&lt;b>🎯 Trả lời cốt lõi:&lt;/b>&lt;br>abc 💡")
        self.assertIn("T_ESCAPED_TAG", codes([card]))

    def test_literal_less_than_entity_is_allowed(self):
        card = basic(back=GOOD_BACK.replace("Sốt cao", "trẻ &lt; 3 tuổi, ANC &lt;500"))
        self.assertNotIn("T_ESCAPED_TAG", codes([card]))

    def test_backslash_before_unicode_arrow_blocks(self):
        # Lỗi PED-47/61/62/63: replace thô `\rightarrow` → `\→`.
        self.assertIn("T_LATEX", codes([basic(back=GOOD_BACK + " Cầu thận \\→ nâu sẫm")]))

    def test_swallowed_escape_remnants_block(self):
        # Lỗi PED-37: "\rightarrow" trong string thường → CR + "ightarrow"; Anki âm thầm xóa CR.
        found = codes([basic(back=GOOD_BACK + " GLUT-1 \rightarrow não")])
        self.assertIn("T_CONTROL_CHAR", found)
        self.assertIn("T_LATEX", found)

    def test_dollar_and_tab_block(self):
        found = codes([basic(back=GOOD_BACK + " $x$"), basic("X-2", front=GOOD_FRONT + "\tA")])
        self.assertIn("T_LATEX", found)
        self.assertIn("T_CONTROL_CHAR", found)

    def test_double_escape_blocks(self):
        self.assertIn("T_DOUBLE_ESCAPE", codes([basic(back=GOOD_BACK + "<b&gt;x")]))
        self.assertIn("T_DOUBLE_ESCAPE", codes([basic(extra="a &amp;lt; b")]))

    def test_unbalanced_tags_block(self):
        self.assertIn("T_TAG_BALANCE", codes([basic(back=GOOD_BACK + "<span style='color:#ffd43b'>x")]))

    def test_escape_keeps_valid_html_and_escapes_less_than(self):
        out = B.escape_angle_brackets("<b>ANC</b> < 500 và <500<br>")
        self.assertEqual(out, "<b>ANC</b> &lt; 500 và &lt;500<br>")
        self.assertNotIn("T_ESCAPED_TAG", codes([basic(back=GOOD_BACK + B.escape_angle_brackets(" <2 tháng"))]))


class BackPurity(unittest.TestCase):
    def test_source_in_back_blocks_but_extra_is_fine(self):
        leaked = basic(back=GOOD_BACK + " (Giáo trình Nhi YTB, trang 38)")
        self.assertIn("P_BACK_SOURCE", codes([leaked]))
        self.assertNotIn("P_BACK_SOURCE", codes([basic(extra="📖 Nguồn: Giáo trình Nhi YTB, trang 38")]))

    def test_cloze_text_is_answer_side(self):
        card = {"id": "C-1", "type": "cloze", "text": "Văn bản gốc mục 1.1: {{c1::IgA}}", "extra": "x"}
        self.assertIn("P_BACK_SOURCE", codes([card]))

    def test_muc_tieu_is_not_a_location(self):
        self.assertNotIn("P_BACK_SOURCE", codes([basic(back=GOOD_BACK + " 3 mục tiêu học tập")]))


class AntiSpoilerCloze(unittest.TestCase):
    def test_partial_list_cloze_flagged(self):
        text = ("Các nguyên nhân đái máu cầu thận gồm: {{c1::viêm cầu thận cấp}}, viêm cầu thận mạn, "
                "và {{c1::bệnh thận IgA}}.")
        self.assertTrue(L.partial_cloze_segments(text))

    def test_numbered_objectives_partial_flagged(self):
        text = ("4 mục tiêu: 1) Định nghĩa và {{c1::nguyên nhân}}; 2) {{c1::Sinh lý bệnh}}; "
                "3) Triệu chứng và {{c1::phân loại}}; 4) Nguyên tắc điều trị và chăm sóc.")
        self.assertTrue(L.partial_cloze_segments(text))

    def test_whole_list_in_one_cloze_is_valid(self):
        text = "Nguyên nhân gồm: {{c1::viêm cầu thận cấp, viêm cầu thận mạn và bệnh thận IgA}}."
        self.assertEqual(L.partial_cloze_segments(text), [])

    def test_numeric_cloze_in_prose_not_flagged(self):
        text = ("Theo JAMA Pediatrics 2023, so với oxy thường, CPAP làm giảm nguy cơ thất bại rút nội khí quản "
                "với tỷ số chênh (OR) là {{c1::0,52}}.")
        self.assertEqual(L.partial_cloze_segments(text), [])


class GovernanceAndModes(unittest.TestCase):
    def test_cloze_only_deck_and_section_without_basic(self):
        cloze = {"id": "C-1", "type": "cloze", "section": "B1", "text": "ANC < {{c1::500}}", "extra": "x"}
        found = codes([cloze, basic("X-2", section="B2")], {"required_sections": ["B1", "B2", "B3"]})
        self.assertIn("G_SECTION_NO_BASIC", found)
        self.assertIn("D_SECTION_MISSING", found)
        self.assertIn("G_CLOZE_ONLY", codes([cloze]))

    def test_missing_ai_explanation_and_colors(self):
        card = basic(front="Câu hỏi trơn?", back="<b>🎯 Trả lời cốt lõi:</b><br>trơn")
        found = codes([card])
        for code in ("G_BACK_STRUCTURE", "G_COLOR_FRONT", "G_COLOR_BACK"):
            self.assertIn(code, found)

    def test_algo_badge_minimum(self):
        algo = [basic(f"A-{i}", badge=L.ALGO_BADGE) for i in range(3)]
        self.assertNotIn("G_ALGO_COUNT", codes(algo))
        self.assertIn("G_ALGO_COUNT", codes(algo[:2]))

    def test_hotfix_turns_governance_into_debt_but_keeps_technical_block(self):
        issues = L.classify(L.lint_cards([basic(front="Trơn?", back="\\→ trơn")]), "hotfix")
        sev = {i.code: i.severity for i in issues}
        self.assertEqual(sev["T_LATEX"], "BLOCK")
        self.assertEqual(sev["G_BACK_STRUCTURE"], "DEBT")
        release = {i.code: i.severity for i in L.classify(L.lint_cards([basic(front="Trơn?")]), "release")}
        self.assertEqual(release["G_COLOR_FRONT"], "BLOCK")

    def test_deck_name_requires_standard_prefix_and_diacritics(self):
        self.assertNotIn("D_DECK_NAME", codes([basic()], {"deck_name": "Nhi khoa Y6::PED-63: Biến thiên bạch cầu"}))
        self.assertNotIn("D_DECK_NAME", codes([basic()], {"deck_name": "Nhi khoa Y6::PED-53: Hạch to (EBM Update)"}))
        self.assertIn("D_DECK_NAME", codes([basic()], {"deck_name": "Nhi khoa Y6::PED-63: Bien thien bach cau"}))
        self.assertIn("D_DECK_NAME", codes([basic()], {"deck_name": "Medical::PED-13_Suy_ho_hap::2026-09-15"}))

    def test_deck_name_follows_each_specialty_root(self):
        noi = "1. Y Khoa - Nội Khoa & Cấp Cứu::02. Tim Mạch::IM-22 Suy tim"
        self.assertNotIn("D_DECK_NAME", codes([basic()], {"deck_name": noi, "specialty": "noi", "id": "IM-22"}))
        # mã bài trong tên deck phải trùng mã bài của manifest
        self.assertIn("D_DECK_NAME", codes([basic()], {"deck_name": noi, "specialty": "noi", "id": "IM-23"}))
        # deck Nội đặt nhầm dưới gốc Nhi
        self.assertIn("D_DECK_NAME", codes([basic()], {"deck_name": "Nhi khoa Y6::IM-22 Suy tim", "specialty": "noi"}))

    def test_duplicate_ids_and_fronts(self):
        found = codes([basic("X-1"), basic("X-1")])
        self.assertIn("T_DUP_ID", found)
        self.assertIn("T_DUP_FRONT", found)


class BuilderEndToEnd(unittest.TestCase):
    def _lesson(self, tmp: Path, cards: list[dict]) -> Path:
        lesson = tmp / "12_Nhi khoa" / "PED-99_Test"
        lesson.mkdir(parents=True, exist_ok=True)
        (lesson / "lesson.json").write_text(json.dumps({
            "id": "PED-99", "specialty": "nhi", "profile": "disease",
            "deck": {"deck_id": 1999000001, "deck_name": "Nhi khoa Y6::PED-99: Bài kiểm thử",
                     "basename": "PED-99_Test", "required_sections": ["B1"], "cards_source": "ped99_cards_data.py"}},
            ensure_ascii=False), encoding="utf-8")
        (lesson / "ped99_cards_data.py").write_text("cards_data = " + json.dumps(cards, ensure_ascii=False), encoding="utf-8")
        return lesson

    def _guids(self, apkg: Path) -> dict:
        with tempfile.TemporaryDirectory() as t, zipfile.ZipFile(apkg) as zf:
            zf.extractall(t)
            db = next(Path(t) / n for n in ("collection.anki21", "collection.anki2") if (Path(t) / n).exists())
            con = sqlite3.connect(db)
            rows = dict(con.execute("select flds, guid from notes").fetchall())
            con.close()
        return {k.split("\x1f")[0]: v for k, v in rows.items()}

    def test_rebuild_after_edit_keeps_guid_so_reimport_updates_instead_of_duplicating(self):
        algo = [basic(f"PED99-A{i}", front=GOOD_FRONT + f" {i}", badge=L.ALGO_BADGE, tier=1) for i in range(3)]
        with tempfile.TemporaryDirectory() as t:
            lesson = self._lesson(Path(t), algo)
            self.assertEqual(B.build(lesson, "release", False, False), 0)
            first = self._guids(lesson / "PED-99_Test.apkg")
            algo[0]["back"] = GOOD_BACK + " (sửa nội dung)"
            self._lesson(Path(t), algo)
            self.assertEqual(B.build(lesson, "release", False, False), 0)
            second = self._guids(lesson / "PED-99_Test.apkg")
            self.assertEqual(sorted(first.values()), sorted(second.values()))
            report = json.loads((lesson / "outputs/verification/PED-99_Test/card-lint.json").read_text(encoding="utf-8"))
            self.assertEqual(report["status"], "PASS")

    def test_release_blocks_and_writes_no_apkg(self):
        with tempfile.TemporaryDirectory() as t:
            lesson = self._lesson(Path(t), [basic("PED99-B1", back="&lt;b>hỏng")])
            self.assertEqual(B.build(lesson, "release", False, False), 2)
            self.assertFalse((lesson / "PED-99_Test.apkg").exists())


if __name__ == "__main__":
    unittest.main()
