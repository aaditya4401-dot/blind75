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
        n = len(coins)

        dp = [[-1]*(amount+1) for _ in range(n+1)]

        ans = self.helper(n-1,amount,coins,dp)

        if ans==float("inf"):
            return -1
        return ans


    def helper(self,ind,target,coins,dp):
        if target==0:
            return 0
        if ind==0:
            if target%coins[0]==0:
                return target//coins[0]
            else:
                return float("inf")
        if dp[ind][target]!=-1:
            return dp[ind][target]
        pick = float("inf")
        if target>=coins[ind]:
            pick = 1+self.helper(ind,target-coins[ind],coins,dp)
        notpick = self.helper(ind-1, target, coins , dp)

        dp[ind][target]= min(pick, notpick)

        return dp[ind][target]



if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
