"""Import paths for the test suite.

Tests live in tests/<category>/ while the problems they import live in
<category>/, so each problem folder goes on sys.path along with the blind75
root (which is what makes `from common.structures import ...` work).
"""

import pathlib
import sys

ROOT = pathlib.Path(__file__).parent.resolve()

sys.path.insert(0, str(ROOT))
for _category in sorted(ROOT.glob("[0-9][0-9]_*")):
    if _category.is_dir():
        sys.path.insert(0, str(_category))
