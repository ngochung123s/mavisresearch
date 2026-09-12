import sys
sys.stdout.reconfigure(encoding="utf-8")
src = open(r"F:\DL\mavisresearch\Bai hoc y khoa\02_Ho tro sinh san ART\41_US_Monitoring_Ovarian_Stimulation\build_slider_deck.py", encoding="utf-8").read()
for w in ["trigger", "freeze-all", "fresh transfer", "fresh ET", "low responder", "high responder", "Clinical pearls", "baseline", "antagonist", "agonist", "OHSS risk", "Decision", "protocol", "LPS"]:
    c = src.count(w)
    if c > 0:
        print(f"{w}: {c}")
