"""
Maximum Subarray  |  LeetCode 53  |  Medium
https://leetcode.com/problems/maximum-subarray/

Find the contiguous subarray (containing at least one number) with the largest
sum, and return that sum.

Example 1:
    Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6                   # the subarray [4, -1, 2, 1]

Example 2:
    Input:  nums = [-1]
    Output: -1

Constraints:
    1 <= len(nums) <= 10^5
    -10^4 <= nums[i] <= 10^4

Hint:
    Kadane's algorithm. Walk left to right holding the best sum of a subarray
    *ending at i*: either extend the previous one, or start fresh at nums[i] --
    whichever is larger. The answer is the max of those values.

Target complexity: O(n) time, O(1) space
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
