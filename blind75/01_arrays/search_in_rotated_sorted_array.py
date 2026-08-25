"""
Search in Rotated Sorted Array  |  LeetCode 33  |  Medium
https://leetcode.com/problems/search-in-rotated-sorted-array/

`nums` is a sorted array of distinct integers, rotated at some unknown pivot.
Return the index of `target`, or -1 if it is absent. O(log n) required.

Example 1:
    Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4

Example 2:
    Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 3
    Output: -1

Constraints:
    1 <= len(nums) <= 5000
    All values are unique.

Hint:
    At any mid, at least one half is properly sorted. Work out which (compare
    nums[lo] with nums[mid]), check whether target falls inside that sorted
    half's range, and discard the other half.

Target complexity: O(log n) time, O(1) space
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_search_in_rotated_sorted_array.py"))]))
