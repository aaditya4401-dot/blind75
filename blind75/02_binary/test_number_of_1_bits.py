"""Tests for Number of 1 Bits. Run: pytest 02_binary/test_number_of_1_bits.py"""
import pytest

from number_of_1_bits import Solution

@pytest.mark.parametrize("n, expected", [
    (11, 3),
    (128, 1),
    (2147483645, 30),
    (1, 1),
    (7, 3),
    (2 ** 31 - 1, 31),
])
def test_hamming_weight(n, expected):
    assert Solution().hammingWeight(n) == expected

