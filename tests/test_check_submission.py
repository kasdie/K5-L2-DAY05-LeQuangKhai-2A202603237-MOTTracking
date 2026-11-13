import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile


SCRIPT = Path(__file__).resolve().parents[1] / "src" / "check_submission.py"


class SubmissionCliTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.archive = Path(self.temp.name) / "mot.zip"

    def write_mot(self, *, width=40, include_images=False):
        lines = [
            f"{frame},{track},{track * 200},100,{width},100,1,1,1"
            for track in (1, 2)
            for frame in range(1, 5)
        ]
        with ZipFile(self.archive, "w") as archive:
            archive.writestr("gt/gt.txt", "\n".join(lines))
            if include_images:
                archive.writestr("img1/synthetic.jpg", b"synthetic test fixture")

    def run_check(self, *options):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--mot", str(self.archive), *options],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

    def test_default_still_requires_five_tracks(self):
        self.write_mot()
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("Có 2 track ID, cần 5", result.stdout)

    def test_valid_count_can_be_explicit_or_flexible(self):
        self.write_mot()
        for options in (("--expected", "2"), ("--allow-any-track-count",)):
            with self.subTest(options=options):
                result = self.run_check(*options)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("Số track ID: 2", result.stdout)

    def test_flexible_count_still_rejects_invalid_boxes(self):
        self.write_mot(width=-1)
        result = self.run_check("--allow-any-track-count")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("box rộng hoặc cao <= 0", result.stdout)

    def test_flexible_count_still_rejects_images(self):
        self.write_mot(include_images=True)
        result = self.run_check("--allow-any-track-count")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("Zip có kèm ảnh", result.stdout)

    def test_count_modes_cannot_be_combined(self):
        self.write_mot()
        result = self.run_check("--expected", "2", "--allow-any-track-count")
        self.assertEqual(result.returncode, 2, result.stderr)

    def test_expected_count_must_be_positive(self):
        self.write_mot()
        result = self.run_check("--expected", "0")
        self.assertEqual(result.returncode, 2, result.stderr)


if __name__ == "__main__":
    unittest.main()
