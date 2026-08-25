"""
Longest Consecutive Sequence  |  LeetCode 128  |  Medium
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array, return the length of the longest sequence of
consecutive integers in it. You must run in O(n) time (so no sorting).

Example 1:
    Input:  nums = [100, 4, 200, 1, 3, 2]
    Output: 4                   # [1, 2, 3, 4]

Example 2:
    Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    Output: 9

Constraints:
    0 <= len(nums) <= 10^5
    -10^9 <= nums[i] <= 10^9

Hint:
    Dump everything into a set. Only start counting from a number that STARTS a
    run -- that is, one where n - 1 is not in the set -- then walk n+1, n+2...
    upward. That guard is what keeps the whole thing linear: every element is
    walked at most once across all runs.

Target complexity: O(n) time, O(n) space
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
