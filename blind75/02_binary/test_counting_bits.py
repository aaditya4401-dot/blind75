"""Tests for Counting Bits. Run: pytest 02_binary/test_counting_bits.py"""
import pytest

from counting_bits import Solution

@pytest.mark.parametrize("n, expected", [
    (2, [0, 1, 1]),
    (5, [0, 1, 1, 2, 1, 2]),
    (0, [0]),
    (1, [0, 1]),
    (8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),
])
def test_count_bits(n, expected):
    assert Solution().countBits(n) == expected


def test_count_bits_large():
    result = Solution().countBits(1000)
    assert len(result) == 1001
    assert result[1000] == bin(1000).count("1")

