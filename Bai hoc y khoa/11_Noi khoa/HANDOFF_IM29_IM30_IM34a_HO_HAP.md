# HANDOFF: BỘ 3 BÀI HÔ HẤP (IM-29 Hen, IM-30 COPD, IM-34a Tâm phế mạn)

## 0. Exact Paths
- **IM-29 (Hen phế quản):**
  - Plan: `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-29_Hen_phe_quan/PLAN_AND_EXECUTION_PROMPT_IM29.md`
  - Output: `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-29_Hen_phe_quan/IM-29_Hen_phe_quan_YYYY-MM-DD_RELEASE_v1.md`
  - Brief: `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-29_Hen_phe_quan/IM-29_Hen_phe_quan_YYYY-MM-DD_RELEASE_v1_RESEARCH_BRIEF.md`
  - Evidence Bundle: `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-29_Hen_phe_quan/outputs/`
- **IM-30 (COPD):**
  - Plan: `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-30_COPD/PLAN_AND_EXECUTION_PROMPT_IM30.md`
  - Output: `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-30_COPD/IM-30_COPD_YYYY-MM-DD_RELEASE_v1.md`
  - Brief: `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-30_COPD/IM-30_COPD_YYYY-MM-DD_RELEASE_v1_RESEARCH_BRIEF.md`
  - Evidence Bundle: `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-30_COPD/outputs/`
- **IM-34a (Tâm phế mạn):**
  - Plan: `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-34a_Tam_phe_man/PLAN_AND_EXECUTION_PROMPT_IM34a.md`
  - Output: `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-34a_Tam_phe_man/IM-34a_Tam_phe_man_YYYY-MM-DD_RELEASE_v1.md`
  - Brief: `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-34a_Tam_phe_man/IM-34a_Tam_phe_man_YYYY-MM-DD_RELEASE_v1_RESEARCH_BRIEF.md`
  - Evidence Bundle: `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-34a_Tam_phe_man/outputs/`

## 1. Quyết định đã khóa (Locked Decisions)
- **Đối tượng:** Sinh viên y khoa, bác sĩ mới, bác sĩ nội khoa tuyến tỉnh (L3_BEGINNER, 10-14k từ/bài).
- **Phân bổ:** 60% giai đoạn ổn định, 40% đợt cấp/mất bù.
- **Giới hạn Deliverable:** CHỈ tạo file bài học Markdown (MD) và các artifact nghiên cứu nội bộ (Research Brief, evidence bundle). **KHÔNG** tạo APKG, DOCX, Anki cards, Knowledge Checks, hay chạy publish build.
- **IM-34a:** Là một mã bài bổ sung (proposed code) chưa có trong danh mục chính thức, cần được user phê duyệt riêng nếu muốn đưa vào catalog.
- **Overlap & Scope:**
  - **IM-29 (Hen):** Tập trung vào tính biến thiên, viêm đường thở, chiến lược ICS-containing. Không dạy sâu COPD.
  - **IM-30 (COPD):** Tập trung vào hô hấp ký cơ bản, phân nhóm GOLD, lựa chọn dụng cụ hít, xử trí đợt cấp an toàn (oxy 88-92%). Phân biệt hen (asthma features). Không dạy điều trị suy tim phải.
  - **IM-34a (Tâm phế mạn):** Tập trung vào chuỗi nhân quả từ bệnh phổi mạn/thiếu oxy đến suy tim phải, phân biệt PH/Cor pulmonale, quản lý oxy dài hạn (LTOT) và lợi tiểu thận trọng.

## 2. Thứ tự thực thi khuyến nghị (Execution Order)
Nên thực thi theo thứ tự sau (từng bài một):
1. **IM-29 (Hen phế quản):** Vì đây là bệnh lý nền tảng về tắc nghẽn đường thở có tính biến thiên, giúp thiết lập các khái niệm cơ bản về thuốc hít (ICS, SABA, LABA) và hô hấp ký.
2. **IM-30 (COPD):** Kế thừa kiến thức từ IM-29 để so sánh, phân biệt (tắc nghẽn cố định vs biến thiên) và mở rộng sang các nhóm thuốc khác (LAMA).
3. **IM-34a (Tâm phế mạn):** Thực thi cuối cùng vì đây là biến chứng muộn của COPD và các bệnh phổi mạn tính khác, đòi hỏi kiến thức nền từ IM-30 và IM-22 (Suy tim).

## 3. Chính sách bằng chứng chung (Shared Evidence Policy)
- **Prose nền tảng:** Không cần gán nhãn.
- **Claims định lượng/khuyến cáo (5-7 claims/bài):** Phải được kiểm chứng qua offline evidence bundle (tạo bằng `evidence_sync.py` từ nguồn official hiện hành).
- **Nguồn:** GINA (Hen), GOLD (COPD), ESC/ERS (PH/Tâm phế mạn). Không dùng NCBI/E-utilities.
- **Nhãn hợp lệ duy nhất:** `[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[FULL TEXT VERIFIED]`, `[GUIDELINE VERIFIED]`. KHÔNG tự bịa nhãn. Nhãn `[FETCHED]` không được support claims định lượng/khuyến cáo. Cấm legacy labels. Yêu cầu kiểm tra authority, version, supersession, license, provenance.
- **Xử lý thiếu bằng chứng:** Nếu không thể kiểm chứng, phải bỏ qua con số chính xác hoặc chuyển thành câu hỏi tự kiểm tra `CẦN TỰ KIỂM CHỨNG`.

## 4. Tiêu chuẩn nghiệm thu chung (Common Acceptance Bar)
- **Độ dài:** 10,000 - 14,000 từ/bài, văn xuôi hoàn chỉnh, không scaffold/stub.
- **Cases:** Chính xác 5 ca lâm sàng/bài, mỗi ca tuân thủ đúng 5 bước: Red flag, Dữ kiện quyết định, Hành động, Monitoring/chuyển tuyến, Why alternatives wrong.
- **Format:** Không dùng Mermaid (dùng ASCII flowcharts), không dùng bảng >= 4 cột.
- **Ngôn ngữ:** Tiếng Việt có dấu chuẩn xác, văn phong y khoa chuyên nghiệp.
- **Dừng lại (Stop conditions):** Hoàn thành file MD bài học và báo cáo kết quả. MD là deliverable học tập duy nhất (brief/bundle nội bộ được phép). Không chạy các bước build/publish. Không update catalog/curriculum. IM-34a approval unchecked.

## 5. Launcher Prompts cho Future Models

### Prompt 1: IM-29 Hen phế quản
```text
Bạn là Medical Writer Agent. Hãy mở và đọc kỹ file plan tại `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-29_Hen_phe_quan/PLAN_AND_EXECUTION_PROMPT_IM29.md`.
Thực thi toàn bộ quy trình nghiên cứu (tạo Research Brief, sync evidence từ GINA/ERS/ATS hiện hành) và viết bài học IM-29 hoàn chỉnh (10-14k từ) theo đúng các yêu cầu trong plan.
Lưu ý: Chỉ tạo file MD bài học và artifacts nội bộ, KHÔNG build package. Chỉ gán 5 nhãn canonical (`[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[FULL TEXT VERIFIED]`, `[GUIDELINE VERIFIED]`) khi có artifact thực sự. Cấm legacy labels.
```

### Prompt 2: IM-30 COPD
```text
Bạn là Medical Writer Agent. Hãy mở và đọc kỹ file plan tại `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-30_COPD/PLAN_AND_EXECUTION_PROMPT_IM30.md`.
Thực thi toàn bộ quy trình nghiên cứu (tạo Research Brief, sync evidence từ GOLD hiện hành) và viết bài học IM-30 hoàn chỉnh (10-14k từ) theo đúng các yêu cầu trong plan.
Lưu ý: Chỉ tạo file MD bài học và artifacts nội bộ, KHÔNG build package. Chỉ gán 5 nhãn canonical (`[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[FULL TEXT VERIFIED]`, `[GUIDELINE VERIFIED]`) khi có artifact thực sự. Cấm legacy labels.
```

### Prompt 3: IM-34a Tâm phế mạn
```text
Bạn là Medical Writer Agent. Hãy mở và đọc kỹ file plan tại `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-34a_Tam_phe_man/PLAN_AND_EXECUTION_PROMPT_IM34a.md`.
Thực thi toàn bộ quy trình nghiên cứu (tạo Research Brief, sync evidence từ ESC/ERS hiện hành) và viết bài học IM-34a hoàn chỉnh (10-14k từ) theo đúng các yêu cầu trong plan.
Lưu ý: Chỉ tạo file MD bài học và artifacts nội bộ, KHÔNG build package. Chỉ gán 5 nhãn canonical (`[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[FULL TEXT VERIFIED]`, `[GUIDELINE VERIFIED]`) khi có artifact thực sự. Cấm legacy labels.
```

## 6. Progress Checklist
- [ ] Hoàn thành IM-29 Hen phế quản
- [ ] Hoàn thành IM-30 COPD
- [ ] Phê duyệt mã bài IM-34a vào catalog (User action)
- [ ] Hoàn thành IM-34a Tâm phế mạn
