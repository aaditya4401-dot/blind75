"""
Longest Increasing Subsequence  |  LeetCode 300  |  Medium
https://leetcode.com/problems/longest-increasing-subsequence/

Return the length of the longest strictly increasing subsequence of `nums`.
A subsequence keeps relative order but need not be contiguous.

Example 1:
    Input:  nums = [10, 9, 2, 5, 3, 7, 101, 18]
    Output: 4                   # [2, 3, 7, 101]

Example 2:
    Input:  nums = [7, 7, 7, 7, 7, 7, 7]
    Output: 1                   # "strictly" increasing

Constraints:
    1 <= len(nums) <= 2500
    -10^4 <= nums[i] <= 10^4

Hint:
    O(n^2): dp[i] = longest subsequence ending at i = 1 + max(dp[j]) over all
    j < i with nums[j] < nums[i].

    O(n log n): keep a list `tails` where tails[k] is the smallest possible tail
    of an increasing subsequence of length k+1. For each number, binary search
    (bisect_left) for its slot -- replace if found, append if it is the new
    largest. len(tails) is the answer. Note tails is NOT itself a valid LIS.

Target complexity: O(n^2) DP, or O(n log n) with patience sorting
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pass
