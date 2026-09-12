import sys

from pptx import Presentation

from qa_pptx import PPTX, slide_text


prs = Presentation(PPTX)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
for idx in [13, 14, 111]:
    text = slide_text(prs.slides[idx - 1])
    print("---", idx)
    print(repr(text[-700:]))
