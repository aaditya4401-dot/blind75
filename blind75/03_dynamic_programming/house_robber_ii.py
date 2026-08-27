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
        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 ,dp2 = [-1]*(n-1) , [-1]*(n-1)


        return max(self.helper(n-2,nums[:n-1],dp1),self.helper(n-2,nums[1:],dp2))

    def helper(self,ind, nums, dp):
        if ind==0:
            return nums[0]
        if ind==1:
            return max(nums[0],nums[1])

        if dp[ind]!=-1:
            return dp[ind]

        rob = nums[ind] + self.helper(ind-2,nums,dp)
        notrob = self.helper(ind-1, nums,dp )

        dp[ind] = max(rob, notrob)

        return dp[ind]


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
