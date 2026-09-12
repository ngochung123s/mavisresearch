"""Build PGT-A Anki APKG với Pastel theme.

Cards loaded from PGT-A_cards.json.
Output: Anki - PGT-A 23 cards - 2026-06-25.apkg
"""
import json
import random
import sys
from pathlib import Path

# Add script folder to path so we can import lesson_builder
SCRIPT_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
sys.path.insert(0, str(SCRIPT_DIR))

from lesson_builder import (
    build_pastel_model_and_deck,
    add_cards_from_json,
    write_apkg,
)

# Paths
BASE = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\02_Ho tro sinh san ART\13_PGT-A_Preimplantation_Genetic_Testing")
CARDS_JSON = BASE / "PGT-A_cards.json"
OUTPUT_APKG = BASE / "Anki - PGT-A 23 cards - 2026-06-25.apkg"

# Random model + deck IDs (để tránh conflict nếu import lại)
MODEL_ID = random.randint(1000000000, 9999999999)
DECK_ID = random.randint(1000000000, 9999999999)

# Build
model, deck = build_pastel_model_and_deck(
    model_id=MODEL_ID,
    model_name="PGT-A Pastel Model",
    deck_id=DECK_ID,
    deck_name="PGT-A - Preimplantation Genetic Testing",
    deck_description="Sàng lọc di truyền tiền làm tổ phôi (Aneuploidy) - 2026-06-25. 23 cards Pastel theme. ASRM 2024, ESHRE 2024, PGT-M, mosaic management, niPGT-A, polar body, time-lapse, AI.",
)

# Add cards
n_cards = add_cards_from_json(deck, model, str(CARDS_JSON), tags="PGT-A aneuploidy")
print(f"  [APKG] Added {n_cards} cards from JSON")

# Write
write_apkg(deck, str(OUTPUT_APKG))
print(f"  [APKG] Saved: {OUTPUT_APKG}")
print(f"  [APKG] Size: {OUTPUT_APKG.stat().st_size} bytes")
