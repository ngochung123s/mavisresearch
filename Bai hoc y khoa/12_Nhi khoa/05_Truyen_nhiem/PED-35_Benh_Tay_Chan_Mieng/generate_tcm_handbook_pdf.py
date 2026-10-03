# -*- coding: utf-8 -*-
"""
generate_tcm_handbook_pdf.py
Tạo tài liệu HTML Sổ tay Lâm sàng Bệnh Tay Chân Miệng (PED-35) và xuất bản sang PDF chuẩn in ấn qua MS Edge Headless.
"""

import os
import sys
import subprocess
import shutil
import fitz  # PyMuPDF

HTML_PATH = r"F:\DL\mavisresearch\Bai hoc y khoa\12_Nhi khoa\05_Truyen_nhiem\PED-35_Benh_Tay_Chan_Mieng\tcm_clinical_master_guide.html"
OUTPUT_DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\12_Nhi khoa\05_Truyen_nhiem\PED-35_Benh_Tay_Chan_Mieng\outputs"
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "SO_TAY_LAM_SANG_TAY_CHAN_MIENG_PED35.pdf")
DESKTOP_PDF = r"C:\Users\THANHANH\Desktop\SO_TAY_LAM_SANG_TAY_CHAN_MIENG_PED35.pdf"

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(EDGE_PATH):
    EDGE_PATH = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

print(f"[*] Sẽ sử dụng Edge: {EDGE_PATH}")
os.makedirs(OUTPUT_DIR, exist_ok=True)
