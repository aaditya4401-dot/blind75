"""
Valid Anagram  |  LeetCode 242  |  Easy
https://leetcode.com/problems/valid-anagram/

Return True if `t` is an anagram of `s` -- the same characters with the same
counts, in any order.

Example 1:
    Input:  s = "anagram", t = "nagaram"
    Output: True

Example 2:
    Input:  s = "rat", t = "car"
    Output: False

Constraints:
    1 <= len(s), len(t) <= 5 * 10^4
    Both consist of lowercase English letters.

Hint:
    Compare character counts (Counter(s) == Counter(t)), after the O(1)
    early-out of len(s) != len(t). Sorting both is O(n log n) and also fine.
    Follow-up worth thinking about: what changes for Unicode input?

Target complexity: O(n) time, O(alphabet) space
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
