"""Regression tests for depth_check.py."""
import tempfile
import unittest
from pathlib import Path

from depth_check import (
    DepthConfig,
    FoundationConfig,
    check_guidelines,
    run_depth_check,
)


class DepthCheckTests(unittest.TestCase):
    def test_metabolic_bone_guidelines_count(self):
        content = "NOGG ISCD USPSTF Endocrine Society NOGG"
        passed, count, found = check_guidelines(content, DepthConfig())
        self.assertTrue(passed)
        self.assertEqual(count, 5)
        self.assertIn("NOGG(2)", found)

    def test_unrelated_prose_does_not_count(self):
        passed, count, found = check_guidelines("ordinary clinical prose", DepthConfig())
        self.assertFalse(passed)
        self.assertEqual(count, 0)
        self.assertEqual(found, [])

    def test_short_lesson_with_all_headings_fails(self):
        content = """\
## 0. Tổng quan
Bài học ngắn.
## 1. Định nghĩa
Định nghĩa ngắn.
## 2. Cơ chế
Cơ chế ngắn.
## 3. Chẩn đoán
Chẩn đoán ngắn.
## 4. Điều trị
Điều trị ngắn.
## 5. Theo dõi
Theo dõi ngắn.
## 6. Tóm tắt
Tóm tắt ngắn.
## 7. Tips
Tips ngắn.
## 8. Bằng chứng
Bằng chứng ngắn.
## 9. Tài liệu tham khảo
1. Paper 1. PMID: 12345678
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "short_lesson.md"
            file_path.write_text(content, encoding="utf-8")
            report = run_depth_check(file_path, FoundationConfig())
            self.assertFalse(report.passed)
            failed_names = [r.name for r in report.results if not r.passed]
            self.assertTrue(any("Total size" in name or "Main sections" in name for name in failed_names))

    def test_long_lesson_with_duplicated_text_fails(self):
        repeated_line = "Đây là dòng văn bản bị lặp đi lặp lại rất nhiều lần để tạo độ dài giả tạo cho bài học y khoa này.\n"
        content = """\
## 0. Tổng quan
## 1. Định nghĩa
## 2. Cơ chế
## 3. Chẩn đoán
## 4. Điều trị
## 5. Theo dõi
## 6. Tóm tắt
## 7. Tips
## 8. Bằng chứng
## 9. Tài liệu tham khảo
### 0.1 Nền tảng tối thiểu cần dùng ngay
```text
A --> B
```
BOX ĐỎ
### Case 1
""" + (repeated_line * 200)

        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "padded_lesson.md"
            file_path.write_text(content, encoding="utf-8")
            report = run_depth_check(file_path, FoundationConfig())
            self.assertFalse(report.passed)
            failed_names = [r.name for r in report.results if not r.passed]
            self.assertTrue(any("padding" in name.lower() for name in failed_names))

    def test_repeated_template_lines_different_number_fails(self):
        template_lines = [
            f"Đoạn văn bản y khoa giải thích chi tiết kiến thức nền tảng dòng thứ {i} giúp học viên nắm vững bản chất vấn đề lâm sàng.\n"
            for i in range(100)
        ]
        content = """\
## 0. Tổng quan
## 1. Định nghĩa
## 2. Cơ chế
## 3. Chẩn đoán
## 4. Điều trị
## 5. Theo dõi
## 6. Tóm tắt
## 7. Tips
## 8. Bằng chứng
## 9. Tài liệu tham khảo
### 0.1 Nền tảng tối thiểu cần dùng ngay
```text
A --> B
```
BOX ĐỎ
### Case 1
""" + "".join(template_lines)

        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "template_padded_lesson.md"
            file_path.write_text(content, encoding="utf-8")
            report = run_depth_check(file_path, FoundationConfig())
            self.assertFalse(report.passed)
            failed_names = [r.name for r in report.results if not r.passed]
            self.assertTrue(any("padding" in name.lower() for name in failed_names))

    def test_lesson_with_placeholders_fails(self):
        content = """\
## 0. Tổng quan
[Mục tiêu 1] Cần bổ sung nội dung.
TODO: Viết thêm phần này.
TBD: Nội dung chưa hoàn thành.
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "placeholder_lesson.md"
            file_path.write_text(content, encoding="utf-8")
            report = run_depth_check(file_path, FoundationConfig())
            self.assertFalse(report.passed)
            failed_names = [r.name for r in report.results if not r.passed]
            self.assertTrue(any("placeholders" in name.lower() for name in failed_names))

    def test_foundation_without_drugs_does_not_fail_dosage(self):
        cfg = FoundationConfig()
        self.assertFalse(cfg.require_drug_dosage)

    def test_valid_deep_lesson_fixture_passes(self):
        sections = []
        sections.append("## 0. TỔNG QUAN\n### 0.1 Nền tảng tối thiểu cần dùng ngay\n")
        sections.append("Tổng quan dịch tễ học và khái niệm lâm sàng cho người mới bắt đầu học y khoa.\n")

        primer_lines = [
            "Sinh lý học tế bào là nền tảng tối thiểu giúp hiểu rõ cơ chế vận chuyển chất qua màng.",
            "Điện thế màng nghỉ được duy trì bởi hoạt động của bơm Na-K ATPase trên màng tế bào.",
            "Khử cực màng xảy ra khi kênh Na phụ thuộc điện thế mở ra cho dòng Na đi vào tế bào.",
            "Tái cực xảy ra khi kênh K mở ra đưa dòng ion K đi ra ngoài tế bào phục hồi điện thế.",
            "Giai đoạn trơ tuyệt đối ngăn chặn các kích thích mới truyền qua trong lúc tế bào tái cực.",
            "Nồng độ calci nội bào tăng cao khởi phát quá trình co cơ tim và cơ trơn thành mạch.",
            "Hệ thần kinh giao cảm kích thích thụ thể beta-1 làm tăng tần số và sức co bóp cơ tim.",
            "Hệ phó giao cảm thông qua dây thần kinh phế vị làm giảm tần số tim và tốc độ dẫn truyền.",
            "Áp lực thẩm thấu máu được duy trì chủ yếu bởi nồng độ natri và glucose trong huyết tương.",
            "Khả năng tự điều hòa của mạch máu giúp duy trì lưu lượng máu tưới các cơ quan quan trọng.",
            "Sự chênh lệch áp lực thủy tĩnh và áp lực keo quyết định sự trao đổi chất tại mao mạch.",
            "Hệ renin-angiotensin-aldosterone đóng vai trò trung tâm trong điều hòa thể tích tuần hoàn.",
            "Angiotensin II gây co mạch mạnh và kích thích vỏ thượng thận tăng tiết hormone aldosterone.",
            "Aldosterone làm tăng tái hấp thu natri và nước tại ống lượn xa và ống góp của nephron.",
            "Hormone chống bài niệu ADH tăng cường gắn nước tại kênh aquaporin-2 ở ống góp.",
            "Sự cân bằng kiềm toan được điều hòa bởi hệ đệm bicarbonate cùng phổi và thận.",
            "Sự suy giảm chức năng bù trừ sẽ dẫn đến các rối loạn chuyển hóa và lâm sàng nghiêm trọng.",
        ]
        sections.extend(primer_lines)

        sections.append("Hội chứng u máu là tình trạng rối loạn cấu trúc mạch máu bẩm sinh.\n")
        sections.append("Bệnh mạch vành là hội chứng suy giảm tưới máu cơ tim do hẹp động mạch.\n")
        sections.append("Creatinine là thông số đánh giá chức năng lọc của hệ thống cầu thận.\n")
        sections.append("eGFR là chỉ số tốc độ lọc ước tính dựa trên creatinine huyết thanh.\n")
        sections.append("Huyết áp là chỉ số áp lực của dòng máu tác động lên thành động mạch.\n")

        sections.append("Cơ chế phân tử: Kênh 1 phân tử → Tế bào mô → Tưới máu mô → Lâm sàng → Phản chứng. Tầng 1 đến Tầng 5.\n")
        sections.append("Chuỗi cơ chế 1: Nguyên nhân A → Tổn thương B → Biến chứng C → Triệu chứng D.\n")
        sections.append("Chuỗi cơ chế 2: Thụ thể E → Enzyme F → Chất trung gian G → Phản ứng H.\n")
        sections.append("Chuỗi cơ chế 3: Yếu tố I → Tín hiệu J → Tổng hợp K → Hiện tượng L.\n")

        sections.append("```text\nA --> B --> C\n```\nBOX ĐỎ: Cảnh báo nguy hiểm cấp cứu khẩn cấp.\n")

        sections.append("## 1. ĐỊNH NGHĨA\n### 1.1 Định nghĩa bệnh\n")
        sections.append("Ví dụ 1: Trường hợp điển hình của bệnh nhân phát hiện sớm.\n")
        sections.append("Ví dụ 2: Biểu hiện lâm sàng ban đầu thường dễ bị bỏ sót.\n")
        sections.append("Ví dụ 3: Cảnh báo các dấu hiệu bất thường trên cận lâm sàng.\n")
        sections.append("Ví dụ 4: Phản ứng phụ không mong muốn sau khi khởi đầu điều trị.\n")
        sections.append("Ví dụ 5: Đột biến gen di truyền ảnh hưởng nghiêm trọng tới tiên lượng.\n")
        sections.append("Ví dụ 6: Biến thể giải phẫu bẩm sinh thường gặp trên thực địa.\n")

        sections.append("Bẫy 1: Học viên hay nhầm giữa chẩn đoán xác định và triệu chứng phụ.\n")
        sections.append("Bẫy 2: Phản ví dụ lâm sàng làm nhiễu kết quả đánh giá ban đầu.\n")
        sections.append("Bẫy 3: Sai lầm phổ biến khi phân tầng mức độ nghiêm trọng.\n")
        sections.append("Bẫy 4: Nhầm lẫn triệu chứng thoáng qua với tổn thương thực thể.\n")
        sections.append("Bẫy 5: Lỗi thường gặp khi phiên giải xét nghiệm chuyên sâu.\n")
        sections.append("Bẫy 6: Cạm bẫy trong theo dõi và đánh giá đáp ứng dài hạn.\n")

        sections.append("## 2. CƠ CHẾ\n### 2.1 Sinh lý chi tiết\n### 2.2 Pathophysiology\n")
        sections.append("Phân tích sinh lý bệnh học diễn tiến phức tạp qua các giai đoạn khác nhau.\n")
        sections.append("Đánh giá tác động của tổn thương tế bào lên chức năng toàn bộ cơ quan.\n")
        sections.append("Sự suy giảm khả năng bù trừ của hệ thống nội môi khi stress kéo dài.\n")

        sections.append("Checkpoint 1: Tự kiểm tra kiến thức về các bước trong chuỗi sinh lý bệnh.\n")
        sections.append("Checkpoint 2: Tự kiểm tra các tiêu chuẩn chẩn đoán quan trọng nhất.\n")
        sections.append("Checkpoint 3: Tự kiểm tra chỉ định và chống chỉ định của liệu pháp.\n")
        sections.append("Checkpoint 4: Kiểm tra nhanh các nguy cơ biến chứng rủi ro cao.\n")

        sections.append("## 3. CHẨN ĐOÁN\n### 3.1 Tiêu chuẩn chẩn đoán\n### 3.2 Phân tầng nguy cơ\n")
        sections.append("Trình bày hệ thống tiêu chuẩn chẩn đoán dựa trên chứng cứ y học.\n")
        sections.append("Phân tích vai trò của từng xét nghiệm trong việc khẳng định chẩn đoán.\n")
        sections.append("Thang điểm phân tầng rủi ro để đưa ra chiến lược xử trí phù hợp.\n")

        sections.append("### Case 1: Ca lâm sàng nam 50 tuổi nhập viện cấp cứu\nLời giải: Phân tích nguyên nhân chẩn đoán và đưa ra phương án xử trí chi tiết.\n")
        sections.append("### Case 2: Ca lâm sàng nữ 65 tuổi theo dõi ngoại trú\nLời giải: Phân tích kết quả cận lâm sàng và đáp án hướng xử trí tối ưu.\n")

        sections.append("## 4. ĐIỀU TRỊ\n### 4.1 Điều trị nội khoa\n### 4.2 Theo dõi điều trị\n")
        sections.append("Nguyên tắc chung trong xây dựng phác đồ điều trị cá thể hóa.\n")
        sections.append("Các nhóm liệu pháp được ưu tiên lựa chọn hàng đầu.\n")
        sections.append("Chiến lược theo dõi hiệu quả và điều chỉnh liều kịp thời.\n")

        sections.append("Mô tả quy trình theo dõi điều trị lâm sàng theo tiêu chuẩn y khoa.\n")

        sections.append("## 5. THEO DÕI\n### 5.1 Đánh giá định kỳ\n")
        sections.append("Lịch trình theo dõi định kỳ đánh giá sự phục hồi của bệnh nhân.\n")
        sections.append("Các chỉ số cận lâm sàng cần kiểm tra lại sau mỗi đợt điều trị.\n")
        sections.append("Dấu hiệu nhận biết sớm nguy cơ tái phát bệnh để can thiệp kịp thời.\n")

        sections.append("## 6. TÓM TẮT\n### 6.1 Tổng kết trọng tâm\n")
        sections.append("Tóm lược các thông điệp lâm sàng cốt lõi cần nhớ sau bài học.\n")
        sections.append("Sơ đồ thuật toán tóm tắt quy trình xử trí nhanh tại phòng khám.\n")
        sections.append("Các mẹo nhỏ giúp nhớ nhanh kiến thức quan trọng khi làm bài.\n")

        sections.append("## 7. TIPS THỰC HÀNH\n")
        tips_lines = [
            "- **Tip 1**: Lấy máu động mạch làm khí máu phải tiến hành đuổi hết khí trong xi-lanh.",
            "- **Tip 2**: Đánh giá điện tâm đồ cần đọc theo đúng thứ tự 7 bước chuẩn.",
            "- **Tip 3**: Kiểm tra chức năng thận trước khi chỉ định thuốc cản quang.",
            "- **Tip 4**: Đánh giá đáp ứng bù trừ hô hấp khi gặp rối loạn toan kiềm.",
            "- **Tip 5**: Theo dõi nồng độ điện giải đồ huyết thanh khi dùng lợi tiểu.",
            "- **Tip 6**: Phân tầng nguy cơ tim mạch trước khi khởi đầu liệu pháp.",
            "- **Tip 7**: Đánh giá mức lọc cầu thận eGFR thay vì chỉ nhìn vào creatinine.",
            "- **Tip 8**: Kiểm tra đường huyết mao mạch ngay khi bệnh nhân hôn mê.",
            "- **Tip 9**: Đọc X-quang ngực thẳng theo thứ tự từ ngoài vào trong.",
            "- **Tip 10**: Đánh giá đáp ứng bù trừ thần kinh thể dịch ở bệnh nhân suy tim.",
            "- **Tip 11**: Hướng dẫn bệnh nhân tuân thủ chế độ ăn giảm muối nghiêm ngặt.",
        ]
        sections.extend(tips_lines)
        sections.append("## 8. BẰNG CHỨNG MỚI\n### 8.1 Guideline updates\n")
        sections.append("Cập nhật các nghiên cứu lâm sàng mới nhất năm 2025-2026.\n")
        sections.append("Tổng quan các khuyến cáo mới nhất từ các hội chuyên khoa uy tín.\n")
        sections.append("Các thử nghiệm lâm sàng ngẫu nhiên đối chứng mới công bố gần đây.\n")
        sections.append("Thay đổi về quan điểm điều trị so với các hướng dẫn trước đây.\n")

        sections.append("## 9. TÀI LIỆU THAM KHẢO\n")
        sections.append("Tổng hợp từ các giáo trình y khoa kinh điển và đồng thuận lâm sàng.\n")

        # Generate unique thematic prose lines without numbered templates
        subjects = ["Bệnh nhân", "Hệ thống tim mạch", "Chức năng thận", "Đội ngũ y tế", "Phác đồ điều trị", "Chỉ số sinh hiệu", "Xét nghiệm máu", "Hình ảnh X-quang", "Liệu pháp oxy", "Đáp ứng viêm"]
        verbs = ["cần được theo dõi", "đóng vai trò quan trọng trong", "ảnh hưởng trực tiếp tới", "giúp cải thiện đáng kể", "thể hiện sự biến đổi", "phản ánh mức độ tổn thương", "yêu cầu đánh giá cẩn thận", "mang lại lợi ích dài hạn", "được ghi nhận trong", "tạo tiền đề cho"]
        contexts = ["quá trình hồi phục chức năng.", "việc phân tầng nguy cơ lâm sàng.", "diễn tiến của bệnh lý mãn tính.", "quyết định can thiệp kịp thời.", "các nghiên cứu thử nghiệm lâm sàng.", "việc phòng ngừa biến chứng nguy hiểm.", "kế hoạch chăm sóc toàn diện.", "đánh giá tiên lượng sống còn.", "thực hành y khoa hằng ngày.", "chuẩn hóa quy trình điều trị."]

        unique_prose = []
        for s in subjects:
            for v in verbs:
                for c in contexts:
                    unique_prose.append(f"{s} {v} {c}")

        full_content = "\n".join(sections) + "\n" + "\n".join(unique_prose)

        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "valid_deep_lesson.md"
            file_path.write_text(full_content, encoding="utf-8")
            report = run_depth_check(file_path, FoundationConfig())
            if not report.passed:
                report.print()
            self.assertTrue(report.passed)


if __name__ == "__main__":
    unittest.main()
