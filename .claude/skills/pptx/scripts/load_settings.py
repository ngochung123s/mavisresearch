#!/usr/bin/env python3
"""Load PPTX skill settings from ../settings.json with defaults."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DEFAULT_SETTINGS: dict[str, Any] = {
    "engine": "pptxgenjs",
    "canvas": "canonical",
    "qa": {
        "checkCanvas": True,
        "checkOverflow": True,
        "checkPageBadge": True,
        "checkPlaceholder": True,
        "checkThinSlides": True,
        "requireSpeakerNotes": False,
        "warnRepeatedCitations": True,
        "requireImageSources": False,
    },
    "medicalTeaching": {
        "enabled": True,
        "requireWhat": True,
        "requireWhy": True,
        "requireRiskIfWrong": True,
    },
    "render": {
        "enabled": False,
        "tryPowerPoint": True,
        "tryLibreOffice": True,
        "requireRenderPass": False,
    },
    "citation": {
        "preferClaimSpecificNotes": True,
        "allowRepeatedPmidFooter": False,
    },
    "output": {
        "saveNextToSource": True,
        "outputFolder": "",
    },
}


def deep_merge(default: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = dict(default)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def default_settings_path() -> Path:
    return Path(__file__).resolve().parents[1] / "settings.json"


def load_settings(path: str | None = None) -> dict[str, Any]:
    settings_path = Path(path) if path else default_settings_path()
    if not settings_path.exists():
        return DEFAULT_SETTINGS.copy()
    data = json.loads(settings_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Settings file must contain a JSON object: {settings_path}")
    return deep_merge(DEFAULT_SETTINGS, data)


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Print resolved PPTX skill settings.")
    parser.add_argument("--config", help="Optional settings.json path")
    args = parser.parse_args()
    print(json.dumps(load_settings(args.config), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
