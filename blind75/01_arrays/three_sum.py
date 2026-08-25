"""
3Sum  |  LeetCode 15  |  Medium
https://leetcode.com/problems/3sum/

Return all unique triplets [nums[i], nums[j], nums[k]] with distinct indices
such that they sum to 0. The solution set must not contain duplicate triplets.

Example 1:
    Input:  nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

Example 2:
    Input:  nums = [0, 1, 1]
    Output: []

Constraints:
    3 <= len(nums) <= 3000
    -10^5 <= nums[i] <= 10^5

Hint:
    Sort first. Fix nums[i], then two-pointer the remaining suffix for a pair
    summing to -nums[i]. Sorting is what makes dedup cheap: skip nums[i] when it
    equals nums[i-1], and after recording a hit advance both pointers past
    their duplicates.

Target complexity: O(n^2) time, O(1) extra space (sorting aside)
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_three_sum.py"))]))
