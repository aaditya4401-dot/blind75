"""Tests for Alien Dictionary. Run: pytest 04_graphs/test_alien_dictionary.py"""
import pytest

from alien_dictionary import Solution

def valid_order(words, order):
    """A returned order is correct if it re-sorts the input into the same list."""
    if len(set(order)) != len(order):
        return False
    if set(order) != set("".join(words)):
        return False
    rank = {c: i for i, c in enumerate(order)}
    keyed = sorted(words, key=lambda w: [rank[c] for c in w])
    return keyed == list(words)


@pytest.mark.parametrize("words", [
    ["wrt", "wrf", "er", "ett", "rftt"],
    ["z", "x"],
    ["z", "x", "y", "w"],
    ["ab", "adc"],
    ["abc"],
])
def test_alien_order_valid(words):
    assert valid_order(words, Solution().alienOrder(words))


@pytest.mark.parametrize("words", [
    ["z", "x", "z"],
    ["abc", "ab"],
    ["a", "b", "a"],
])
def test_alien_order_invalid(words):
    assert Solution().alienOrder(words) == ""

