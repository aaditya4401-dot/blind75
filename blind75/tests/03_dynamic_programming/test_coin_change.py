"""Tests for Coin Change. Run: pytest 03_dynamic_programming/test_coin_change.py"""
import pytest

from coin_change import Solution

@pytest.mark.parametrize("coins, amount, expected", [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1, 3, 4], 6, 2),
    ([2, 5, 10, 1], 27, 4),
    ([186, 419, 83, 408], 6249, 20),
    ([5], 5, 1),
])
def test_coin_change(coins, amount, expected):
    assert Solution().coinChange(coins, amount) == expected

