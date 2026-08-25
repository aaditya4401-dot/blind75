"""
Missing Number  |  LeetCode 268  |  Easy
https://leetcode.com/problems/missing-number/

`nums` holds n distinct numbers drawn from the range [0, n]. Return the one
number in that range that is missing.

Example 1:
    Input:  nums = [3, 0, 1]
    Output: 2

Example 2:
    Input:  nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    Output: 8

Constraints:
    1 <= len(nums) <= 10^4
    All values are unique and lie in [0, n].

Hint:
    Two O(1)-space answers. Gauss: n * (n + 1) // 2 minus sum(nums). Or XOR
    every index 0..n together with every value -- each present number cancels
    itself and only the missing one survives (XOR avoids any overflow concern).

Target complexity: O(n) time, O(1) space
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pass
