"""Check the approved structural contract for one lesson profile."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PROFILE_REQUIREMENTS = {
    "foundation": {
        "headings": (
            "tổng quan",
            "định nghĩa",
            "cơ chế",
            "chẩn đoán",
            "theo dõi",
            "tóm tắt",
            "tips",
            "tài liệu tham khảo",
        ),
        "markers": {
            "prerequisite": "nền tảng tối thiểu cần dùng ngay",
            "flowchart": "```text",
            "case": "case 1",
            "safety": "box đỏ",
        },
    },
    "disease": {
        "headings": (
            "tổng quan",
            "định nghĩa",
            "cơ chế",
            "chẩn đoán",
            "điều trị",
            "theo dõi",
            "tóm tắt",
            "tips",
            "bằng chứng",
            "tài liệu tham khảo",
        ),
        "markers": {
            "prerequisite": "nền tảng tối thiểu cần dùng ngay",
            "flowchart": "```text",
            "case": "case 1",
            "safety": "box đỏ",
        },
    },
    "pharmacology": {
        "headings": (
            "tổng quan",
            "bản đồ nhóm thuốc",
            "kê đơn thực hành",
            "kháng lợi tiểu",
            "tổng kết",
            "tips",
            "tài liệu tham khảo",
        ),
        "markers": {
            "prerequisite_link": "sinh lý nephron",
            "segment_map": "nkcc2",
            "monitoring": "creatinine",
            "flowchart": "```text",
            "case": "case 1",
            "safety": "box đỏ",
        },
    }
}


def check_profile_content(profile: str, content: str) -> list[str]:
    """Return every unmet structural requirement for an approved profile."""
    requirements = PROFILE_REQUIREMENTS[profile]
    normalized = content.casefold()
    headings = {
        match.group(1).strip().casefold()
        for match in re.finditer(r"^#{2,3}\s+(.+?)\s*$", content, re.MULTILINE)
    }
    failures = [
        f"missing heading: {heading}"
        for heading in requirements["headings"]
        if not any(heading in actual for actual in headings)
    ]
    failures.extend(
        f"missing {name}: {marker}"
        for name, marker in requirements["markers"].items()
        if marker not in normalized
    )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check an approved lesson profile")
    parser.add_argument("profile", choices=sorted(PROFILE_REQUIREMENTS))
    parser.add_argument("lesson", type=Path)
    args = parser.parse_args()

    try:
        content = args.lesson.read_text(encoding="utf-8")
    except OSError as exc:
        parser.error(str(exc))

    failures = check_profile_content(args.profile, content)
    if failures:
        print(f"PROFILE BLOCKED: {args.profile}", file=sys.stderr)
        print("\n".join(f"- {failure}" for failure in failures), file=sys.stderr)
        return 1

    print(f"PROFILE PASS: {args.profile}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
