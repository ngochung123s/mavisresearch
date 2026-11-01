"""
Wrapper proxy forwarding to hungmed/build_unified_med_library.py
"""
import subprocess
import sys
from pathlib import Path

target = Path(__file__).resolve().parent.parent / "hungmed" / "build_unified_med_library.py"
sys.exit(subprocess.call([sys.executable, str(target)] + sys.argv[1:]))
