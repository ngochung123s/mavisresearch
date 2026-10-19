import subprocess
import sys
import tempfile
import unittest
from textwrap import dedent
from pathlib import Path

from profile_check import check_profile_content


FOUNDATION = """## Tổng quan
## Định nghĩa
## Cơ chế
## Chẩn đoán
## Theo dõi
## Tóm tắt
## Tips
## Tài liệu tham khảo
### 0.1 Nền tảng tối thiểu cần dùng ngay
```text
A --> B
```
BOX ĐỎ
### Case 1
"""

PHARMACOLOGY = """## Tổng quan
## Bản đồ nhóm thuốc
## Kê đơn thực hành
## Theo dõi
## Tổng kết
## Tips
## Tài liệu tham khảo
```text
A --> B
```
BOX ĐỎ
### Case 1
"""


class ProfileCheckTest(unittest.TestCase):
    def test_foundation_passes_and_missing_marker_fails(self):
        self.assertEqual(check_profile_content("foundation", FOUNDATION), [])
        failures = check_profile_content("foundation", FOUNDATION.replace("Case 1", "Tình huống"))
        self.assertIn("missing case: case 1", failures)
        failures = check_profile_content("foundation", FOUNDATION.replace("## Cơ chế\n", ""))
        self.assertIn("missing heading: cơ chế", failures)

    def test_pharmacology_passes_and_missing_marker_fails(self):
        self.assertEqual(check_profile_content("pharmacology", PHARMACOLOGY), [])
        failures = check_profile_content("pharmacology", PHARMACOLOGY.replace("BOX ĐỎ", "Cảnh báo"))
        self.assertIn("missing safety: box đỏ", failures)

    def test_pharmacology_is_generic_not_diuretic_specific(self):
        statin = PHARMACOLOGY.replace("Bản đồ nhóm thuốc", "Bản đồ nhóm thuốc hạ lipid")
        self.assertEqual(check_profile_content("pharmacology", statin), [])

    def test_vietnamese_case_markers_pass(self):
        for variant in ("Ca lâm sàng 1", "### Ca 1", "### Ca lâm sàng"):
            text = FOUNDATION.replace("### Case 1", variant if variant.startswith("###") else "### " + variant)
            if variant == "Ca lâm sàng 1":
                text = FOUNDATION.replace("### Case 1", "Ca lâm sàng 1")
            self.assertEqual(check_profile_content("foundation", text), [], variant)

    def test_flowchart_bare_fence_with_glyphs_and_mermaid_pass(self):
        ascii_tree = FOUNDATION.replace("```text\nA --> B\n```", "```\nA\n├── B\n└── C\n```")
        self.assertEqual(check_profile_content("foundation", ascii_tree), [])
        mermaid = FOUNDATION.replace("```text", "```mermaid")
        self.assertEqual(check_profile_content("foundation", mermaid), [])

    def test_flowchart_bare_fence_without_glyphs_fails(self):
        plain = FOUNDATION.replace("```text\nA --> B\n```", "```\nA và B\n```")
        self.assertIn("missing flowchart: ```text", check_profile_content("foundation", plain))
        one_glyph = FOUNDATION.replace("```text\nA --> B\n```", "```\nA → B\n```")
        self.assertIn("missing flowchart: ```text", check_profile_content("foundation", one_glyph))

    def test_heading_terms_in_prose_do_not_satisfy_profile(self):
        prose_only = FOUNDATION.replace("## Tóm tắt\n", "Tóm tắt nằm trong đoạn văn, không phải heading.\n")
        failures = check_profile_content("foundation", prose_only)
        self.assertIn("missing heading: tóm tắt", failures)

    def test_disease_passes_and_missing_safety_fails(self):
        disease = dedent("""\
        ## Tổng quan
        ## Định nghĩa
        ## Cơ chế
        ## Chẩn đoán
        ## Điều trị
        ## Theo dõi
        ## Tóm tắt
        ## Tips
        ## Bằng chứng
        ## Tài liệu tham khảo
        ### 0.1 Nền tảng tối thiểu cần dùng ngay
        ```text
        A --> B
        ```
        BOX ĐỎ
        ### Case 1
        """)
        self.assertEqual(check_profile_content("disease", disease), [])
        failures = check_profile_content("disease", disease.replace("BOX ĐỎ", "Cảnh báo"))
        self.assertIn("missing safety: box đỏ", failures)

    def test_cli_fail_closes(self):
        script = Path(__file__).with_name("profile_check.py")
        with tempfile.TemporaryDirectory() as directory:
            lesson = Path(directory) / "lesson.md"
            lesson.write_text(FOUNDATION, encoding="utf-8")
            passed = subprocess.run([sys.executable, str(script), "foundation", str(lesson)], capture_output=True, text=True)
            self.assertEqual(passed.returncode, 0, passed.stderr)
            self.assertIn("PROFILE PASS", passed.stdout)

            lesson.write_text("## Tổng quan", encoding="utf-8")
            blocked = subprocess.run([sys.executable, str(script), "foundation", str(lesson)], capture_output=True, text=True)
            self.assertEqual(blocked.returncode, 1)
            self.assertIn("PROFILE BLOCKED", blocked.stderr)


if __name__ == "__main__":
    unittest.main()
