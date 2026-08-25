"""
Best Time to Buy and Sell Stock  |  LeetCode 121  |  Easy
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

`prices[i]` is the price of a stock on day i. Choose a single day to buy and a
later day to sell. Return the maximum profit; return 0 if no profit is possible.

Example 1:
    Input:  prices = [7, 1, 5, 3, 6, 4]
    Output: 5                   # buy at 1 (day 1), sell at 6 (day 4)

Example 2:
    Input:  prices = [7, 6, 4, 3, 1]
    Output: 0                   # prices only fall, so never buy

Constraints:
    1 <= len(prices) <= 10^5
    0 <= prices[i] <= 10^4

Hint:
    One pass. Carry the cheapest price seen so far; at every day the best profit
    ending today is price - cheapest_so_far. Keep the running max of that.

Target complexity: O(n) time, O(1) space
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
