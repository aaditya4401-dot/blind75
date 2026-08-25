"""Tests for Reverse Bits. Run: pytest 02_binary/test_reverse_bits.py"""
import pytest

from reverse_bits import Solution

@pytest.mark.parametrize("n, expected", [
    (43261596, 964176192),
    (4294967293, 3221225471),
    (0, 0),
    (1, 2147483648),
    (2147483648, 1),
    (4294967295, 4294967295),
])
def test_reverse_bits(n, expected):
    assert Solution().reverseBits(n) == expected

