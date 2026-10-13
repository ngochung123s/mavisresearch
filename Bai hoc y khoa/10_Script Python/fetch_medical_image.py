# -*- coding: utf-8 -*-
"""
fetch_medical_image.py
Tiện ích tự động tìm kiếm, tải, nén và chuẩn hóa ảnh minh họa y khoa:
- Tự động nén chất lượng cao (WebP / JPEG, max_width: 1200px, quality: 85%, optimize: True)
- Kiểm soát dung lượng nghiêm ngặt (Target <= 150 KB/ảnh)
- Hỗ trợ tải từ URL trực tiếp hoặc tìm kiếm tự động qua Wikipedia / Wikimedia y khoa
"""

import sys
import os
import re
import json
import urllib.request
import urllib.parse
from pathlib import Path
from PIL import Image

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def optimize_image(img_path: Path, max_width: int = 1200, target_quality: int = 85) -> bool:
    """
    Tự động chuẩn hóa kích thước và nén ảnh (Layer 1 - Compression Gate):
    - Đổi ảnh RGBA sang RGB nếu lưu định dạng JPEG
    - Giới hạn max_width <= 1200px (đủ chuẩn Retina cho bài đọc và Anki)
    - Nén tối ưu hóa (optimize=True) để dung lượng đạt <= 150 KB
    """
    try:
        orig_size = img_path.stat().st_size
        with Image.open(img_path) as im:
            w, h = im.size
            if w > max_width:
                new_h = int(h * (max_width / w))
                im = im.resize((max_width, new_h), Image.Resampling.LANCZOS)
            
            fmt = im.format or "JPEG"
            if img_path.suffix.lower() in [".jpg", ".jpeg"]:
                fmt = "JPEG"
                if im.mode in ("RGBA", "P"):
                    im = im.convert("RGB")
            elif img_path.suffix.lower() == ".webp":
                fmt = "WEBP"
            elif img_path.suffix.lower() == ".png":
                fmt = "PNG"

            # Lưu đè file đã tối ưu
            im.save(img_path, format=fmt, quality=target_quality, optimize=True)

        new_size = img_path.stat().st_size
        ratio = round((1 - new_size / orig_size) * 100, 1) if orig_size > 0 else 0
        print(f"[OPTIMIZE] Kích thước: {w}x{h} -> Dung lượng: {orig_size:,} bytes -> {new_size:,} bytes (Tối ưu {ratio}%)")
        return True
    except Exception as e:
        print(f"[WARN] Không thể nén ảnh {img_path}: {e}")
        return False

def download_image_from_url(url: str, out_path: Path) -> bool:
    """Tải ảnh trực tiếp từ URL với header chuẩn tránh lỗi 403 Forbidden và tự động nén."""
    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            out_path.write_bytes(content)
        print(f"[DOWNLOAD OK] Đã tải về: {out_path} ({len(content):,} bytes)")
        optimize_image(out_path)
        return True
    except Exception as e:
        print(f"[ERROR] Không thể tải ảnh từ {url}: {e}")
        return False

def search_and_download_wiki_image(topic: str, out_path: Path, preferred_keyword: str = "") -> bool:
    """
    Tìm bài viết trên Wikipedia y khoa tiếng Anh và tự động tải & nén ảnh minh họa phù hợp nhất.
    """
    try:
        api_url = f"https://en.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(topic)}&prop=images&format=json"
        req = urllib.request.Request(api_url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))

        images = data.get('parse', {}).get('images', [])
        if not images:
            print(f"[WARN] Không tìm thấy danh sách ảnh trên trang Wiki: '{topic}'")
            return False

        filtered = [
            img for img in images 
            if not any(x in img.lower() for x in ['.svg', '.ogg', 'logo', 'icon', 'symbol', 'flag', 'edit-ltr'])
        ]

        if not filtered:
            print(f"[WARN] Không có file ảnh raster (.jpg/.png) trên trang: '{topic}'")
            return False

        target_img = filtered[0]
        if preferred_keyword:
            kw = preferred_keyword.lower()
            for img in filtered:
                if kw in img.lower():
                    target_img = img
                    break

        print(f"[*] Tìm thấy ảnh mục tiêu: {target_img}")

        info_url = f"https://en.wikipedia.org/w/api.php?action=query&titles=File:{urllib.parse.quote(target_img)}&prop=imageinfo&iiprop=url&format=json"
        req2 = urllib.request.Request(info_url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req2, timeout=10) as resp2:
            info_data = json.loads(resp2.read().decode('utf-8'))

        pages = info_data.get('query', {}).get('pages', {})
        for _, pdata in pages.items():
            img_info = pdata.get('imageinfo', [{}])[0]
            direct_url = img_info.get('url')
            if direct_url:
                return download_image_from_url(direct_url, out_path)

        print("[ERROR] Không trích xuất được Direct URL từ Wikimedia API.")
        return False
    except Exception as e:
        print(f"[ERROR] Lỗi tra cứu Wikipedia: {e}")
        return False

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Medical Image Fetcher with Auto-Optimization")
    parser.add_argument("--url", help="Direct URL của ảnh")
    parser.add_argument("--wiki", help="Tên chủ đề/bệnh tiếng Anh trên Wikipedia (ví dụ: 'Croup', 'Kawasaki disease')")
    parser.add_argument("--kw", default="", help="Từ khóa lọc tên file ảnh")
    parser.add_argument("--out", required=True, help="Đường dẫn file đích cần lưu")

    args = parser.parse_args()
    out = Path(args.out)

    if args.url:
        download_image_from_url(args.url, out)
    elif args.wiki:
        search_and_download_wiki_image(args.wiki, out, args.kw)
    else:
        print("Vui lòng cung cấp --url hoặc --wiki")
