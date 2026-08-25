"""Makes `from common.structures import ...` work from any test file.

pytest already puts each test's own directory on sys.path (so a test can do
`from two_sum import Solution`); this adds the blind75 root so the shared
helpers resolve too.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
