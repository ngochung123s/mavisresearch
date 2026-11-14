# GEMINI.md — Antigravity Workspace Guidelines for `F:\DL\mavisresearch\`

> **Owner**: Bác sĩ Đỗ Văn Ngọc Hưng 🍅 🐈‍⬛  
> **Workspace**: `F:\DL\mavisresearch\`  
> **Remote Origin**: `https://github.com/ngochung123s/mavisresearch.git` (nhánh `main`)  
> **Deployment**: Cloudflare Pages -> [dvnhmed.pages.dev](https://dvnhmed.pages.dev)  
> **Xác thực Git**: Windows Git Credential Manager (`credential.helper = manager`)

---

## 1. Quy trình Git Push & Deploy chuẩn

Khi hoàn thành bài học y khoa hoặc cập nhật hệ thống:

```bash
# 1. Biên dịch dữ liệu thư viện HungMed
python "F:\DL\mavisresearch\Bai hoc y khoa\hungmed\build_unified_med_library.py"

# 2. Stage các thay đổi trong Bài học y khoa
git -C "F:\DL\mavisresearch" add "Bai hoc y khoa/"

# 3. Commit theo chuẩn Conventional Commits
git -C "F:\DL\mavisresearch" commit -m "feat(<chuyen_khoa>): phat hanh <ma_bai>"

# 4. Push lên GitHub (tự động trigger Cloudflare Pages deploy lên dvnhmed.pages.dev)
git -C "F:\DL\mavisresearch" push origin main
```

---

## 2. Nguyên tắc an toàn dữ liệu
- ❌ **TUYỆT ĐỐI KHÔNG ghi file vào ổ C:** (ổ C sắp đầy). Mọi output phải nằm trong `F:\DL\mavisresearch\`.
- ✅ Mọi script/output liên quan y khoa → `F:\DL\mavisresearch\Bai hoc y khoa\`.
- ✅ Tuân thủ nghiêm ngặt các Gate kiểm định y khoa và chuẩn thẻ Anki theo `RULES_LESSON_APKG.md`.
