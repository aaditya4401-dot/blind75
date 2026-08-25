"""
Combination Sum IV  |  LeetCode 377  |  Medium
https://leetcode.com/problems/combination-sum-iv/

Given an array of distinct integers `nums` and a `target`, return the number of
possible combinations that add up to target. Different orderings count as
different combinations (so it is really permutations).

Example 1:
    Input:  nums = [1, 2, 3], target = 4
    Output: 7
            (1,1,1,1) (1,1,2) (1,2,1) (1,3) (2,1,1) (2,2) (3,1)

Example 2:
    Input:  nums = [9], target = 3
    Output: 0

Constraints:
    1 <= len(nums) <= 200
    1 <= nums[i] <= 1000, all distinct
    1 <= target <= 1000

Hint:
    dp[t] = number of ways to reach t; dp[0] = 1. Because order matters, the
    target loop must be OUTSIDE and the nums loop inside:
        for t in 1..target: for n in nums: if n <= t: dp[t] += dp[t - n]
    Swapping the loop order counts unordered combinations instead -- that
    distinction is the whole point of this problem.

Target complexity: O(target * len(nums)) time, O(target) space
"""

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        pass
