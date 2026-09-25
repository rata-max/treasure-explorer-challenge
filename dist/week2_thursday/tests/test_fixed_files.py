"""The provided files must stay identical to the released copies.

Line endings are normalised before hashing, so a Windows checkout with CRLF
line endings still passes. Evaluation always uses clean official copies.
"""

from __future__ import annotations

import hashlib
import unittest
from pathlib import Path


EXPECTED = {
    "agent.py": "5a4f94114db5fb154416efb7aeaa1a487ac0b0b83067372dda9d4e5468abe55d",
    "policy_helpers.py": "00e3958aaa591fe1ad74448b8e3e92205304391474d03f832762c046c90ccf7a",
    "treasure_explorer/engine.py": "2bbdf5c01689aef09c1dab2a9eb6efa363ddb4b848413b3a469c093037a672fb",
    "treasure_explorer/runner.py": "c0b916ef97fc5b0891708a9b0a49aa136a79d6478807cbe1b46c4d4503a8a9a7",
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
