"""
telegram_bot.py
Trình tự động hóa tải tài liệu, hình ảnh độ nét cao từ Telegram Bot cá nhân về máy tính:
- Bot: @ngochungagentbot
- Hỗ trợ tải ảnh nén (photo) và file gốc (document/image/pdf).
"""
import os
import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path

BOT_TOKEN = "8978937454:AAG4ja9pm8bqGDErFL2JKGVcJSyne20BhiY"
API_BASE = f"https://api.telegram.org/bot{BOT_TOKEN}"
FILE_BASE = f"https://api.telegram.org/file/bot{BOT_TOKEN}"

DEFAULT_DOWNLOAD_DIR = Path(r"C:\Users\THANHANH\Desktop\pedytb_raw")

def api_request(endpoint: str, params: dict = None) -> dict:
    url = f"{API_BASE}/{endpoint}"
    if params:
        data = json.dumps(params).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"})
    else:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))

def send_message(chat_id: int, text: str):
    try:
        api_request("sendMessage", {"chat_id": chat_id, "text": text})
    except Exception as e:
        print(f"Error sending message: {e}")

def get_file_url(file_id: str) -> str:
    res = api_request("getFile", {"file_id": file_id})
    if res.get("ok"):
        file_path = res["result"]["file_path"]
        return f"{FILE_BASE}/{file_path}"
    raise RuntimeError(f"Cannot get file path for {file_id}")

def download_file(file_url: str, dest_path: Path):
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(file_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        dest_path.write_bytes(resp.read())

def fetch_media(dest_dir: Path = DEFAULT_DOWNLOAD_DIR, send_reply: bool = True) -> list[Path]:
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    updates = api_request("getUpdates")
    if not updates.get("ok"):
        print("Lỗi lấy updates từ Telegram.")
        return []

    items = updates.get("result", [])
    if not items:
        print("Chưa có tin nhắn mới nào gửi tới Bot.")
        return []

    downloaded = []
    processed_chat_ids = set()
    latest_update_id = 0

    for u in items:
        uid = u.get("update_id", 0)
        if uid > latest_update_id:
            latest_update_id = uid

        msg = u.get("message") or u.get("channel_post")
        if not msg:
            continue

        chat_id = msg.get("chat", {}).get("id")
        if chat_id:
            processed_chat_ids.add(chat_id)

        # 1. Photo (lấy ảnh có kích thước lớn nhất ở cuối mảng)
        if "photo" in msg:
            photos = msg["photo"]
            best_photo = photos[-1]
            fid = best_photo["file_id"]
            file_url = get_file_url(fid)
            ext = file_url.split(".")[-1] or "jpg"
            out_file = dest_dir / f"tele_{msg.get('message_id')}_{best_photo.get('file_unique_id')}.{ext}"
            print(f"Đang tải ảnh: {out_file.name} ({best_photo.get('width')}x{best_photo.get('height')})...")
            download_file(file_url, out_file)
            downloaded.append(out_file)

        # 2. Document (nếu gửi ảnh dưới dạng File/Document để giữ 100% chất lượng gốc)
        elif "document" in msg:
            doc = msg["document"]
            fid = doc["file_id"]
            file_name = doc.get("file_name", f"doc_{msg.get('message_id')}")
            file_url = get_file_url(fid)
            out_file = dest_dir / file_name
            print(f"Đang tải tài liệu gốc: {out_file.name} ({doc.get('file_size', 0) // 1024} KB)...")
            download_file(file_url, out_file)
            downloaded.append(out_file)

    if downloaded and send_reply:
        for cid in processed_chat_ids:
            send_message(cid, f"✅ Agent Mavis đã nhận thành công {len(downloaded)} tệp/ảnh vào Desktop! Đang tiến hành xử lý...")

    print(f"\n=> Tổng cộng đã tải {len(downloaded)} tệp vào: {dest_dir}")
    return downloaded

if __name__ == "__main__":
    fetch_media()
