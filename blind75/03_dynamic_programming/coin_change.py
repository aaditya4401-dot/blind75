"""
Coin Change  |  LeetCode 322  |  Medium
https://leetcode.com/problems/coin-change/

Given coin denominations `coins` and a total `amount`, return the fewest coins
needed to make up that amount, or -1 if it cannot be made. You have an infinite
supply of each coin.

Example 1:
    Input:  coins = [1, 2, 5], amount = 11
    Output: 3                   # 5 + 5 + 1

Example 2:
    Input:  coins = [2], amount = 3
    Output: -1

Constraints:
    1 <= len(coins) <= 12
    1 <= coins[i] <= 2^31 - 1
    0 <= amount <= 10^4

Hint:
    Unbounded knapsack. dp[x] = fewest coins for x; dp[0] = 0 and everything
    else starts at infinity. For each x, dp[x] = 1 + min(dp[x - c]) over coins
    c <= x. Greedy (take the biggest coin first) is wrong -- coins=[1,3,4],
    amount=6 gives 4+1+1 instead of 3+3.

Target complexity: O(amount * len(coins)) time, O(amount) space
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pass
