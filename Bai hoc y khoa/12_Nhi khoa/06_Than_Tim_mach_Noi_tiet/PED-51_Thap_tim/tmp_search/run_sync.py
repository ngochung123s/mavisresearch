"""P3 driver: run canonical evidence_sync with longer HTTP timeout.

Why: Europe PMC responds slowly tonight (>5s); evidence_sync.request defaults
to timeout=5 and fail-closes. This driver ONLY extends the timeout to 60s via
runtime patch — no repo script is modified, no check is weakened, failures
still fail closed (no retry, no fallback).
"""
import functools
import sys

sys.path.insert(0, "10_Script Python")

from pathlib import Path

import evidence_sync

_orig_request = evidence_sync.request


@functools.wraps(_orig_request)
def _slow_request(url, headers=None, timeout=5):
    return _orig_request(url, headers=headers, timeout=60)


evidence_sync.request = _slow_request

pmids = ["25908771", "19246689", "37914787", "34767321",
         "28834488", "38625703", "17034886", "17671255", "27188830"]
base = Path("12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-51_Thap_tim")
bundle = evidence_sync.sync(
    pmids, base / "evidence_bundle.json",
    base / "raw_cache", base / "official_manifest.json")
print("SYNC OK — records:", len(bundle.get("records", {})))
for k in sorted(bundle.get("records", {}).keys()):
    print(" ", k)
