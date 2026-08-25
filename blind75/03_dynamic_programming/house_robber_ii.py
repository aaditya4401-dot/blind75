"""
House Robber II  |  LeetCode 213  |  Medium
https://leetcode.com/problems/house-robber-ii/

Same as House Robber, except the houses are arranged in a circle -- the first
and last house are adjacent, so you cannot rob both.

Example 1:
    Input:  nums = [2, 3, 2]
    Output: 3                   # not 2 + 2, they are neighbours

Example 2:
    Input:  nums = [1, 2, 3, 1]
    Output: 4

Constraints:
    1 <= len(nums) <= 100
    0 <= nums[i] <= 1000

Hint:
    Solve House Robber twice on straight lines -- nums[:-1] (skip the last
    house) and nums[1:] (skip the first) -- and take the larger. Guard the
    single-house case, where both slices are empty.

Target complexity: O(n) time, O(1) space
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
