"""The provided files must stay identical to the released copies.

Line endings are normalised before hashing, so a Windows checkout with CRLF
line endings still passes. Evaluation always uses clean official copies.
"""

from __future__ import annotations

import hashlib
import unittest
from pathlib import Path


EXPECTED = {
    "agent.py": "0dfeb9ac2524df12846e6cafc7f4e7ddf78085560d88abeb217c54c7d3ca92e2",
    "policy_helpers.py": "d47bd7211d8b84ba8a8c0b6944bcc3ba4b61f63bb96ffef8487d69b112efd0c3",
    "treasure_explorer/engine.py": "0356841bc149921de68824f64a4e92bf55543a29bf9a7cfd3936e89dd85e2831",
    "treasure_explorer/runner.py": "c0b916ef97fc5b0891708a9b0a49aa136a79d6478807cbe1b46c4d4503a8a9a7",
    "evaluate.py": "fec89a4f92e00765e9eb8b7de9946319727f06eac6b153cbe88e2b5d1a0dd208",
    "treasure_explorer/generator.py": "3a813e6f5f2cd10100f92fef03d2edd96cb99f68b1d3673bdfe78870e2b69e7a",
}


def normalised_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


class FixedFileTests(unittest.TestCase):
    def test_provided_files_are_unchanged(self):
        root = Path(__file__).parents[1]
        for name, expected in EXPECTED.items():
            self.assertEqual(
                expected,
                normalised_sha256(root / name),
                f"{name} is fixed; restore it and edit only student_policy.py",
            )


if __name__ == "__main__":
    unittest.main()
