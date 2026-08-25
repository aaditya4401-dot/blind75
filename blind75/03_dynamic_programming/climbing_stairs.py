"""
Climbing Stairs  |  LeetCode 70  |  Easy
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase of `n` steps. Each move you climb either 1 or 2
steps. In how many distinct ways can you reach the top?

Example 1:
    Input:  n = 2
    Output: 2                   # 1+1, 2

Example 2:
    Input:  n = 3
    Output: 3                   # 1+1+1, 1+2, 2+1

Constraints:
    1 <= n <= 45

Hint:
    To land on step n you arrived from n-1 or n-2, so ways(n) = ways(n-1) +
    ways(n-2) -- Fibonacci. Roll it forward with two variables instead of an
    array; recursion without memoization is exponential.

Target complexity: O(n) time, O(1) space
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        pass
