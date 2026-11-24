"""Tests for the absurd-invention pitch entry.

Run: python3 -m pytest tests/ -q   (or: python3 tests/test_entry.py)
"""

import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(REPO, "main.py")

SENTENCE = (
    "My washing machine returns one sock a week with a ransom note "
    "demanding softer detergent."
)


class TestEntry(unittest.TestCase):
    def run_program(self, out_dir):
        env = dict(os.environ, OUTPUT_DIR=out_dir)
        result = subprocess.run(
            [sys.executable, MAIN], env=env, capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return os.path.join(out_dir, "entry.txt")

    def test_output_matches_sentence(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.run_program(tmp)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            self.assertEqual(text, SENTENCE)

    def test_gate_one_sentence_max_220_chars(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.run_program(tmp)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            self.assertTrue(1 <= len(text) <= 220, len(text))
            self.assertTrue(text.strip(), "entry must not be only whitespace")
            # exactly one sentence: one terminal period, at the end
            self.assertEqual(text.count("."), 1)
            self.assertTrue(text.endswith("."))
            self.assertNotIn("!", text)
            self.assertNotIn("?", text)

    def test_output_is_plain_utf8_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.run_program(tmp)
            with open(path, "rb") as f:
                raw = f.read()
            raw.decode("utf-8")  # raises if not valid UTF-8
            self.assertEqual(raw, SENTENCE.encode("utf-8"))

    def test_no_trailing_newline_or_extra_whitespace(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.run_program(tmp)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            self.assertEqual(text, text.strip())
            self.assertEqual(len(text), 89)


if __name__ == "__main__":
    unittest.main()
