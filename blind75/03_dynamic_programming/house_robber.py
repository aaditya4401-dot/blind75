"""
House Robber  |  LeetCode 198  |  Medium
https://leetcode.com/problems/house-robber/

Each house holds `nums[i]` money, but robbing two adjacent houses trips the
alarm. Return the maximum you can steal.

Example 1:
    Input:  nums = [1, 2, 3, 1]
    Output: 4                   # rob houses 0 and 2

Example 2:
    Input:  nums = [2, 7, 9, 3, 1]
    Output: 12                  # rob houses 0, 2 and 4

Constraints:
    1 <= len(nums) <= 100
    0 <= nums[i] <= 400

Hint:
    At each house the choice is rob it (nums[i] + best up to i-2) or skip it
    (best up to i-1). Take the max. Two rolling variables are enough -- no array
    needed.

Target complexity: O(n) time, O(1) space
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*(len(nums))

        return self.helper(len(nums)-1,nums,dp)

    def helper(self, ind, nums, dp):
        if ind==0:
            return nums[ind]
        if dp[ind]!=-1:
            return dp[ind]
        rob , notrob= 0,0
        if ind>=2:
            rob = nums[ind] + self.helper(ind-2,nums,dp)
        if ind>=1:
            notrob = self.helper(ind-1,nums, dp)

        dp[ind] = max(rob,notrob)
        return dp[ind]
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
