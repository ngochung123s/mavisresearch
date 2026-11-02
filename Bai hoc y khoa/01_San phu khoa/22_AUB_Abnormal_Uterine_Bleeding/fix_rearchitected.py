# -*- coding: utf-8 -*-
import re

p = "F:/DL/mavisresearch/Bai hoc y khoa/01_San phu khoa/22_AUB_Abnormal_Uterine_Bleeding/build_rearchitected_ob22_cards.py"
text = open(p, encoding="utf-8").read()

# Replace LaTeX tokens
text = text.replace(r"$\\rightarrow$", "→")
text = text.replace(r"\\rightarrow", "→")
text = text.replace("$", "")

# Remove PMID from back
text = text.replace("PMID 36053280", "Tsakiridis 2022")

# Also, let's fix asks:
# In build_rearchitected_ob22_cards.py, add_basic was called with asks=...
# Let's inspect how asks issues are checked in card_lint.py.
# In card_lint.py:
# asks is checked by asks_issues(c).
# asks is only needed if 🎯 has facet labels (is_facet_label).
# If asks is None and there are facet labels -> G_ASKS_MISSING.
# If asks is provided -> each ask MUST be in Front!
# If asks is not None, but front doesn't have it -> G_ASKS_NOT_IN_FRONT.
# To avoid G_ASKS_NOT_IN_FRONT, we can either:
# 1) Make sure Front contains the ask strings, OR
# 2) Change the labels in 🎯 so they don't start with facet words (e.g. prefix with "• " or concept name), OR
# 3) Ensure Front explicitly asks the facets!

open(p, "w", encoding="utf-8").write(text)
print("Saved clean file")
