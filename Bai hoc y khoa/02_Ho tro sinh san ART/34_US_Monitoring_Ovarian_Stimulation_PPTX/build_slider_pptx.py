import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).parent
ENGINE = ROOT.parents[1] / "10_Script Python" / "slider3636.py"
DECK = ROOT / "Sieu_am_theo_doi_kich_thich_buong_trung_slider3636.deck.json"
OUT = ROOT / "Sieu_am_theo_doi_kich_thich_buong_trung_slider3636_2026-07-03.pptx"


spec = importlib.util.spec_from_file_location("slider3636", ENGINE)
slider = importlib.util.module_from_spec(spec)
spec.loader.exec_module(slider)

slider.set_theme(
    palette_name="Medical Teal",
    font_name="Arial",
    size_preset="Large",
    show_pagenum=False,
)

deck = json.loads(DECK.read_text(encoding="utf-8"))
path, count = slider.build_presentation(deck, str(OUT))
print(f"OK: {count} slides -> {path}")
