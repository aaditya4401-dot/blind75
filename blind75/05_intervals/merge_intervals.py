"""
Merge Intervals  |  LeetCode 56  |  Medium
https://leetcode.com/problems/merge-intervals/

Given an array of intervals, merge all overlapping intervals and return the
non-overlapping intervals that cover all the input.

Example 1:
    Input:  intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    Output: [[1, 6], [8, 10], [15, 18]]

Example 2:
    Input:  intervals = [[1, 4], [4, 5]]
    Output: [[1, 5]]            # touching counts as overlapping

Constraints:
    1 <= len(intervals) <= 10^4
    0 <= start <= end <= 10^4

Hint:
    Sort by start -- everything falls out after that. Walk the sorted list: if
    the current interval starts at or before the last merged one's end, extend
    that end to max(both ends); otherwise start a new block.

Target complexity: O(n log n) time, O(n) space
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_merge_intervals.py"))]))
