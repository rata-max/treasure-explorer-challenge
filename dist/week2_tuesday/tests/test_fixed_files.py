from __future__ import annotations

import hashlib
import unittest
from pathlib import Path


EXPECTED = {
    "agent.py": "5a4f94114db5fb154416efb7aeaa1a487ac0b0b83067372dda9d4e5468abe55d",
    "policy_helpers.py": "0314d6fded77b9503b752ab13cc0042666ff1bca6eb8d57ab932ba32dd56c7a8",
}


class FixedFileTests(unittest.TestCase):
    def test_provided_files_are_unchanged(self):
        root = Path(__file__).parents[1]
        for name, expected in EXPECTED.items():
            actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
            self.assertEqual(
                expected,
                actual,
                f"{name} is fixed; restore it and edit only student_policy.py",
            )


if __name__ == "__main__":
    unittest.main()
