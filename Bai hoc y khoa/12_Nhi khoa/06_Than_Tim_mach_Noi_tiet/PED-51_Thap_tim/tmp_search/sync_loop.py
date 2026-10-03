"""P3 looper: full clean evidence_sync attempts spaced 5 min apart (max 12).

Each attempt is a complete fail-closed sync run (no resume, no partial
bundle, no fallback) — equivalent to manually re-running "sync lại sau khi
provider phục hồi". Stops on first success.
"""
import subprocess
import sys
import time

for attempt in range(1, 13):
    print(f"[sync_loop] attempt {attempt}/12", flush=True)
    r = subprocess.run(
        [sys.executable,
         "12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-51_Thap_tim/tmp_search/run_sync.py"],
        capture_output=True, text=True)
    print(r.stdout[-800:] if r.stdout else "", flush=True)
    if r.returncode == 0:
        print("[sync_loop] SUCCESS", flush=True)
        break
    print(f"[sync_loop] failed, sleeping 300s ({r.stderr[-200:] if r.stderr else ''})",
          flush=True)
    time.sleep(300)
else:
    print("[sync_loop] ALL ATTEMPTS FAILED", flush=True)
