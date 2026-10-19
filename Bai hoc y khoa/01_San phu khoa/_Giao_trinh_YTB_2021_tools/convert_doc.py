"""Chuyển giáo trình Sản .doc → .docx bằng Word (chỉ đọc file gốc), số thứ tự tự động → chữ thật."""
from pathlib import Path
import pythoncom
import win32com.client

SRC = Path(r"F:\DL\BG_ĐAI_HỌC_BM_4_12_2021_FINAL_S_Repaired_Đã_sửa_chữa.doc")
OUT = Path(r"F:\DL\san_khoa_reextract\BG_SAN_KHOA_2021.docx")
OUT.parent.mkdir(parents=True, exist_ok=True)

pythoncom.CoInitialize()
word = win32com.client.DispatchEx("Word.Application")
word.Visible = False
word.DisplayAlerts = 0
try:
    doc = word.Documents.Open(str(SRC), ConfirmConversions=False, ReadOnly=True, AddToRecentFiles=False, Visible=False)
    print("paragraphs:", doc.Paragraphs.Count, "tables:", doc.Tables.Count, "inline shapes:", doc.InlineShapes.Count, "shapes:", doc.Shapes.Count)
    doc.ConvertNumbersToText()  # "1." / "-" của danh sách tự động thành chữ (chỉ trong bản sao, không lưu vào .doc)
    doc.SaveAs2(str(OUT), FileFormat=16)  # wdFormatXMLDocument
    doc.Close(SaveChanges=0)
    print("saved", OUT, OUT.stat().st_size)
finally:
    word.Quit()
