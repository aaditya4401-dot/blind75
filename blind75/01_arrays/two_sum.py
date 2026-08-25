"""
Two Sum  |  LeetCode 1  |  Easy
https://leetcode.com/problems/two-sum/

Given an array of integers `nums` and an integer `target`, return the indices of
the two numbers that add up to `target`.

Each input has exactly one solution, and you may not use the same element twice.
The answer may be returned in any order.

Example 1:
    Input:  nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]              # nums[0] + nums[1] == 9

Example 2:
    Input:  nums = [3, 2, 4], target = 6
    Output: [1, 2]

Constraints:
    2 <= len(nums) <= 10^4
    -10^9 <= nums[i], target <= 10^9

Hint:
    Brute force checks every pair: O(n^2). Trade space for time -- walk the array
    once, and for each number ask "have I already seen target - n?" A dict from
    value -> index answers that in O(1).

Target complexity: O(n) time, O(n) space
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index , num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp],index]
            seen[num]=index

        return []


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
