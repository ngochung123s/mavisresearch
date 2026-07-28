"""Regression tests for guideline detection in depth_check."""
import unittest

from depth_check import DepthConfig, check_guidelines


class GuidelineDetectionTests(unittest.TestCase):
    def test_metabolic_bone_guidelines_count(self):
        content = "NOGG ISCD USPSTF Endocrine Society NOGG"
        passed, count, found = check_guidelines(content, DepthConfig())
        self.assertTrue(passed)
        self.assertEqual(count, 5)
        self.assertIn("NOGG(2)", found)

    def test_unrelated_prose_does_not_count(self):
        passed, count, found = check_guidelines("ordinary clinical prose", DepthConfig())
        self.assertFalse(passed)
        self.assertEqual(count, 0)
        self.assertEqual(found, [])


if __name__ == "__main__":
    unittest.main()
