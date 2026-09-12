# PIPELINE_MASTER.md — Sổ tay Vận hành Toàn bộ Pipeline Bài học Y khoa
**Ngày tạo:** 2026-07-26 | **Cập nhật:** sau vụ audit Gemini (IBS 6 Part)
**Mục đích:** Mô tả toàn bộ quy trình từ A-Z: ai chạy cái gì, lệnh gì, file nào, ở đâu.

---

## 🗺️ TỔNG QUAN PIPELINE 5 TẦNG

```text
                    [BÁC SĨ GIAO ĐỀ BÀI]
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│ TẦNG 0: PREFLIGHT — NGƯỜI VẬN HÀNH CHẠY SCRIPT              │
│ python preflight_claim_check.py <BRIEF> --topic "..."        │
│ → Exit 0 mới được đi tiếp. BLOCK → sửa Brief.               │
└──────────────────────────┬───────────────────────────────────┘
                           │ EXIT 0
                           ▼
┌──────────────────────────────────────────────────────────────┐
│ TẦNG 1: RESEARCH — MAVIS TỰ ĐỘNG (dùng tool NCBI/PubMed)    │
│ - Tìm paper, fetch abstract                                  │
│ - Tạo RESEARCH_BRIEF.md (có Quote + tag 5 bậc)              │
│ - Báo cáo bác sĩ duyệt Brief                                 │
└──────────────────────────┬───────────────────────────────────┘
                           │ Bác sĩ duyệt Brief
                           ▼
┌──────────────────────────────────────────────────────────────┐
│ TẦNG 2: EXECUTE — LLM VIẾT BÀI (Gemini/DeepSeek/Claude)    │
│ - Copy STRICT_EXECUTE_PROMPT.md vào system prompt            │
│ - Dán RESEARCH_BRIEF.md vào phần [RESEARCH BRIEF]            │
│ - LLM viết file .md bài học / QA                             │
└──────────────────────────┬───────────────────────────────────┘
                           │ LLM trả bài
                           ▼
┌──────────────────────────────────────────────────────────────┐
│ TẦNG 3: VERIFY — NGƯỜI VẬN HÀNH CHẠY SCRIPT                │
│ python verify_all_pmids.py <file.md>                         │
│ python verify_claim_vs_abstract.py <file.md>                 │
│ python citation_audit.py <file.md>                           │
│ python verify_diacritics.py <file.md>                        │
│ → Tất cả Exit 0 mới PASS.                                    │
└──────────────────────────┬───────────────────────────────────┘
                           │ ALL EXIT 0
                           ▼
┌──────────────────────────────────────────────────────────────┐
│ TẦNG 4: POST-MORTEM — AUDIT CUỐI CÙNG                       │
│ (script post_mortem_audit.py — đang phát triển)              │
│ → Tỷ lệ claim-abstract match ≥ 90% mới PASS                  │
└──────────────────────────┬───────────────────────────────────┘
                           │ PASS
                           ▼
                    [BÀN GIAO CHO BÁC SĨ]
```

---

## 🛠️ BẢNG LỆNH THAM CHIẾU NHANH

Tất cả script nằm trong: `F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\`

| Bước | Lệnh | Ai chạy | Khi nào |
|---|---|---|---|
| **Preflight** | `python preflight_claim_check.py <RESEARCH_BRIEF.md> --topic "Irritable Bowel Syndrome"` | Mavis / Bác sĩ | Sau khi có Brief, trước khi đưa cho LLM |
| **Verify PMID tồn tại** | `python verify_all_pmids.py <file.md>` | Mavis / Bác sĩ | Sau khi LLM viết xong |
| **Verify claim-abstract** | `python verify_claim_vs_abstract.py <file.md>` | Mavis / Bác sĩ | Sau khi LLM viết xong |
| **Citation audit** | `python citation_audit.py <file.md>` | Mavis / Bác sĩ | Sau khi LLM viết xong |
| **Verify dấu tiếng Việt** | `python verify_diacritics.py` | Mavis / Bác sĩ | Sau khi LLM viết xong |

---

## 📋 VAI TRÒ CỦA TỪNG FILE PROMPT / RULE

| File | Dành cho AI? | Dành cho người? | Mục đích |
|---|---|---|---|
| **`STRICT_EXECUTE_PROMPT.md`** | ✅ Copy vào system prompt của LLM | ✅ Đọc để hiểu luật | Dạy LLM cách viết không ảo giác |
| **`RESEARCH_BRIEF_TEMPLATE.md`** | ❌ | ✅ Đọc để tạo Brief | Khuôn mẫu tạo Brief có Quote + tag |
| **`WORKFLOW.md`** | ❌ | ✅ Đọc để vận hành | Checklist 12+ bước cho mỗi bài mới |
| **`AGENTS.md`** | ✅ Mavis đọc khi khởi động | ✅ Đọc để hiểu quy tắc | Quy tắc cứng cho toàn bộ workspace |
| **`SEARCH_STRATEGY.md`** | ✅ Mavis đọc để search | ✅ Tham khảo | Chiến lược tìm kiếm PubMed 6 bước |

---

## ⚡ CÔNG THỨC NHANH CHO 1 BÀI MỚI (CHEAT SHEET)

```bash
# BƯỚC 1: Mavis tạo thư mục + Research Brief
mkdir "F:\DL\mavisresearch\Bai hoc y khoa\11_Noi khoa\IM-XX_Ten_bai"

# BƯỚC 2: Mavis search PubMed + fetch abstract + viết Brief
# (Mavis tự làm, dùng NCBI E-utilities)

# BƯỚC 3: Chạy Preflight
python "10_Script Python/preflight_claim_check.py" ^
  "11_Noi khoa/IM-XX_Ten_bai/RESEARCH_BRIEF.md" ^
  --topic "Disease Name"

# BƯỚC 4: Đưa Brief + STRICT_EXECUTE_PROMPT.md cho LLM
# - Copy STRICT_EXECUTE_PROMPT.md → system prompt
# - Dán RESEARCH_BRIEF.md → [RESEARCH BRIEF]
# - LLM viết bài

# BƯỚC 5: Verify đầu ra
python "10_Script Python/verify_all_pmids.py" "11_Noi khoa/IM-XX_Ten_bai/Part_01_....md"
python "10_Script Python/verify_claim_vs_abstract.py" "11_Noi khoa/IM-XX_Ten_bai/Part_01_....md"
python "10_Script Python/citation_audit.py" "11_Noi khoa/IM-XX_Ten_bai/Part_01_....md"
python "10_Script Python/verify_diacritics.py"

# BƯỚC 6: Bàn giao cho bác sĩ
```

---

## 🚨 QUY TẮC KHẨN CẤP: KHI NÀO DỪNG PIPELINE?

| Tín hiệu | Hành động |
|---|---|
| Preflight exit ≠ 0 | **DỪNG.** Sửa Brief. Không đưa cho LLM. |
| Verify PMID exit ≠ 0 | **DỪNG.** PMID giả. Xóa hoặc thay PMID thật. |
| Verify claim-abstract exit ≠ 0 | **DỪNG.** Claim không khớp abstract. Downgrade tag hoặc xóa claim. |
| Citation audit > 0 BLOCK | **DỪNG.** Paper sai chủ đề hoặc journal kém. Sửa citation. |
| Diacritics < 80% | **CẢNH BÁO.** Thêm dấu tiếng Việt. Không block nhưng phải sửa. |
