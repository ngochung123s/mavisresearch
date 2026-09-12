import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_pipeline
from evidence_bundle import content_hash
from publish_gate import DEFAULT_DEPTH_CONTRACTS, PROFILE_GATES


class ReleaseRunnerTest(unittest.TestCase):
    def test_runner_generates_real_manifest_and_reaches_publish_ready(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            brief = root / "brief.md"
            lesson = root / "lesson_RELEASE_v1.md"
            cards = root / "lesson_RELEASE_v1.cards.v2.json"
            guidelines = root / "guidelines.json"
            outputs = root / "outputs"
            bundle = root / "bundle.json"
            raw = root / "raw.json"
            raw.write_text("{}", encoding="utf-8")
            import hashlib
            digest = hashlib.sha256(raw.read_bytes()).hexdigest()
            now = "2099-01-01T00:00:00Z"
            bundle_data = {
                "schema_version": "1.0", "created_at": now, "providers": ["fixture"], "cache_root": str(root),
                "records": {"pmid:12345678": {"exists": True, "identifiers": {"pmid": "12345678", "doi": "10.1000/fixture"}, "providers": ["europe_pmc_metadata", "openalex", "crossref_retraction_watch"], "raw_sha256": [digest], "metadata_checked_at": now, "integrity": {"status": "clean", "checked_at": now, "corrections": [], "provider": "crossref_retraction_watch"}}},
                "raw_objects": [{"provider": "fixture", "retrieved_at": now, "sha256": digest, "path": "raw.json", "media_type": "application/json", "license": "metadata-only"}], "content_hash": "",
            }
            bundle_data["content_hash"] = content_hash(bundle_data)
            bundle.write_text(json.dumps(bundle_data), encoding="utf-8")
            contract = {
                "profile": "foundation",
                "mode": "L3_BEGINNER",
                "required_gates": list(PROFILE_GATES["foundation"]),
                "lesson_depth_contract": dict(DEFAULT_DEPTH_CONTRACTS["foundation"]),
                "not_applicable": [],
                "approved_exemptions": [],
            }
            brief.write_text(
                "## 0. Lesson profile & release contract\n\n```json\n"
                + json.dumps(contract)
                + "\n```\n\n## 1. Sources\n",
                encoding="utf-8",
            )
            lesson.write_text("Bài học tiếng Việt có dấu. PMID: 12345678 [ABSTRACT VERIFIED]", encoding="utf-8")
            cards.write_text(json.dumps([{"type": "basic", "front": "Câu hỏi?", "back": "Trả lời có dấu."}]), encoding="utf-8")
            guidelines.write_text("{}", encoding="utf-8")

            original_run = build_pipeline.run

            def fake_run(command, timeout=300):
                command = [str(value) for value in command]
                script = Path(command[1]).name if len(command) > 1 else ""
                if script == "publish_gate.py":
                    return original_run(command, timeout)
                if script == "build_apkg.py":
                    Path(command[command.index("--output") + 1]).write_bytes(b"fake-apkg")
                if script == "md_to_docx.py":
                    Path(command[3]).write_bytes(b"fake-docx")
                if script == "make_knowledge_check.py":
                    out = Path(command[command.index("--output-dir") + 1])
                    out.mkdir(parents=True, exist_ok=True)
                    stem = cards.stem.replace(".cards", "").replace(".v2", "")
                    (out / f"{stem}_knowledge_check.md").write_text("five sections", encoding="utf-8")
                    (out / f"{stem}_knowledge_check_answer_key.md").write_text("answers", encoding="utf-8")
                    (out / f"{stem}_knowledge_check_score.json").write_text(json.dumps({
                        "total_questions": 5,
                        "section_counts": {str(index): 1 for index in range(5)},
                        "status": "not_graded",
                    }), encoding="utf-8")
                if "--json-out" in command:
                    Path(command[command.index("--json-out") + 1]).write_text(json.dumps({"status": "PASS"}), encoding="utf-8")
                stdout = json.dumps({"summary": {"total": 1, "pass": 1, "warn": 0, "block": 0}}) if script == "citation_audit.py" else "PASS"
                return subprocess.CompletedProcess(command, 0, stdout, "")

            argv = [
                "build_pipeline.py", "--brief", str(brief), "--lesson", str(lesson),
                "--cards", str(cards), "--guidelines", str(guidelines), "--evidence-bundle", str(bundle), "--outputs", str(outputs),
            ]
            with patch.object(sys, "argv", argv), patch.object(build_pipeline, "run", side_effect=fake_run), patch.object(build_pipeline, "verify_apkg", return_value=(1.0, 10, 10, 1, 1)), patch.object(build_pipeline, "count_words_classified", return_value=(10, 0, 1)):
                code = build_pipeline.main()

            self.assertEqual(code, 0)
            manifest = outputs / "verification" / lesson.stem / "gate-results.json"
            rows = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertEqual({row["gate"] for row in rows}, set(PROFILE_GATES["foundation"]))
            self.assertTrue(all(row["status"] == "PASS" and row["exit_code"] == 0 for row in rows))
            self.assertTrue(all(row["inputs"] and row["artifacts"] for row in rows))


if __name__ == "__main__":
    unittest.main()
