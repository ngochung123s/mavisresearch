"""Regression tests for mcq_lint.py."""
import unittest

from mcq_lint import lint_bank, lint_item


def item(qid, options, correct, text="Trẻ 6 tháng sốt, ho, khò khè.\nCăn nguyên nào có khả năng nhất?", **extra):
    return {"id": qid, "text": text, "options": options, "correct": correct, "explanation": "Giải thích.", **extra}


def codes(issues):
    return {i["code"] for i in issues}


class ItemTests(unittest.TestCase):
    def test_key_much_longer_than_distractors_blocks(self):
        q = item("q1", ["RSV", "Cúm A", "Phế cầu gây viêm phổi thùy với đông đặc và khí phế quản đồ", "hMPV"], 2)
        issues, _ = lint_item(q, 4)
        self.assertIn("length_cue_long", codes(issues))

    def test_balanced_options_pass_length_check(self):
        q = item("q2", ["Virus hợp bào hô hấp", "Metapneumovirus người", "Adenovirus týp 7", "Mycoplasma pneumoniae"], 0)
        issues, _ = lint_item(q, 4)
        self.assertNotIn("length_cue_long", codes(issues))

    def test_all_of_the_above_and_combination_options_block(self):
        q = item("q3", ["RSV", "hMPV", "Cả A và B", "Tất cả các ý trên"], 0)
        issues, _ = lint_item(q, 4)
        self.assertEqual(sum(i["code"] == "banned_option" for i in issues), 2)

    def test_absolute_word_only_in_distractor_warns(self):
        q = item("q4", ["Luôn luôn cần kháng sinh", "Điều trị hỗ trợ là chính", "Cần corticoid toàn thân", "Cần khí dung adrenalin"], 1)
        issues, _ = lint_item(q, 4)
        self.assertIn("absolute_in_distractor", codes(issues))

    def test_clang_phrase_only_in_key_warns(self):
        q = item("q5", ["Bẫy khí tiểu phế quản", "Đông đặc phế nang", "Hoại tử biểu mô", "Xơ hóa mô kẽ"], 0,
                 text="Trẻ 3 tháng có hình ảnh bẫy khí trên phim.\nCơ chế nào giải thích?")
        issues, _ = lint_item(q, 4)
        self.assertIn("clang", codes(issues))

    def test_invalid_key_index_blocks(self):
        issues, feats = lint_item(item("q6", ["a1", "b1", "c1", "d1"], 4), 4)
        self.assertIn("key_index", codes(issues))
        self.assertEqual(feats, {})

    def test_lowercase_negative_leadin_warns(self):
        q = item("q7", ["RSV", "hMPV", "Adenovirus", "Rhinovirus"], 0, text="Trẻ ho.\nTác nhân nào không gây viêm tiểu phế quản?")
        issues, _ = lint_item(q, 4)
        self.assertIn("negative_not_emphasised", codes(issues))


class BankTests(unittest.TestCase):
    def test_bank_where_key_is_usually_longest_blocks(self):
        qs = [item(f"q{i}", ["RSV", "hMPV", "Cúm", "Phế cầu nhóm huyết thanh 19A"], 3) for i in range(12)]
        for i, q in enumerate(qs):
            q["text"] = f"Ca {i}.\nCăn nguyên nào?"
        report = lint_bank({"id": "b", "questions": qs}, 4)
        self.assertIn("bank_key_longest", codes(report["issues"]))
        self.assertGreater(report["stats"]["cue_guess_accuracy"], 0.9)

    def test_duplicate_ids_block(self):
        qs = [item("same", ["a1", "b1", "c1", "d1"], 0, text="Ca 1.\nHỏi?"), item("same", ["a1", "b1", "c1", "d1"], 1, text="Ca 2.\nHỏi?")]
        report = lint_bank({"id": "b", "questions": qs}, 4)
        self.assertIn("duplicate_id", codes(report["issues"]))

    def test_bank_where_key_is_never_longest_blocks(self):
        qs = [item(f"q{i}", ["Virus hợp bào hô hấp", "hMPV týp A", "Adeno týp 7", "Phế cầu 19A"], i % 4, text=f"Ca {i}.\nCăn nguyên nào?") for i in range(16)]
        for q in qs:
            if q["correct"] == 0:
                q["correct"] = 1
        report = lint_bank({"id": "b", "questions": qs}, 4)
        self.assertIn("bank_key_never_longest", codes(report["issues"]))


if __name__ == "__main__":
    unittest.main()
