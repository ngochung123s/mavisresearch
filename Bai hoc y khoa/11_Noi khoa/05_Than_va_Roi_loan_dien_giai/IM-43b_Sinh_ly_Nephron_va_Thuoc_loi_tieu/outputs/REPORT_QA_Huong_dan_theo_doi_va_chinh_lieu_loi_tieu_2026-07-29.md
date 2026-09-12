# Báo cáo Package-level: QA Hướng dẫn theo dõi và chỉnh liều lợi tiểu

Ngày: 2026-07-29

## Các file đã tạo
1. `QA_Huong_dan_theo_doi_va_chinh_lieu_loi_tieu_2026-07-29.md`: QA Markdown tuân thủ template, không có bảng phức tạp, không dùng Mermaid.
2. `QA_Huong_dan_theo_doi_va_chinh_lieu_loi_tieu_2026-07-29.cards.v2.json`: File JSON chứa 80 thẻ Anki (loại basic) bao phủ toàn bộ nội dung QA (từ khung chung, cách đánh giá, từng nhóm thuốc, từng bệnh cảnh, khóa nephron nối tiếp, thuật toán chỉnh liều đến các red flags).
3. `outputs/Anki - QA_Huong_dan_theo_doi_va_chinh_lieu_loi_tieu_2026-07-29.apkg`: File APKG được build thành công từ file JSON.

## Chi tiết Verification
- **Thẻ Anki**: 80 notes / 80 cards.
- **Tiếng Việt**: 96.0% (1765/1839 từ có dấu) -> PASS.
- **Lệnh đã chạy**: `python "F:/DL/mavisresearch/Bai hoc y khoa/10_Script Python/build_apkg.py" "QA_Huong_dan_theo_doi_va_chinh_lieu_loi_tieu_2026-07-29.cards.v2.json" --output "outputs/Anki - QA_Huong_dan_theo_doi_va_chinh_lieu_loi_tieu_2026-07-29.apkg" --verify`
- **Gate đã chạy**: Chỉ chạy build APKG và verify tiếng Việt qua script.
- **Giới hạn verification**:
  - Không tự gắn nhãn `[FULL TEXT VERIFIED]` hoặc các nhãn không hợp lệ.
  - Nhãn `[GUIDELINE VERIFIED]` được sử dụng cho các mốc theo dõi của NHS SPS và KDIGO do đã được cung cấp trong prompt (không tự fetch).
  - Package này **chưa phải là PUBLISH READY** hoàn toàn nếu yêu cầu evidence bundle canonical (do chưa có bước fetch nguồn trực tiếp qua E-utilities).

## Kết quả kiểm tra SQLite trong APKG
- Source count = Note count = Card count = 80.
- 0 missing source pairs.
- 0 unexpected pairs.
- 0 blank pairs.
- 0 duplicate pairs.
