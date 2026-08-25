"""Tests for Decode Ways. Run: pytest 03_dynamic_programming/test_decode_ways.py"""
import pytest

from decode_ways import Solution

@pytest.mark.parametrize("s, expected", [
    ("12", 2),
    ("226", 3),
    ("06", 0),
    ("0", 0),
    ("10", 1),
    ("100", 0),
    ("2101", 1),
    ("27", 1),
    ("11106", 2),
    ("1", 1),
    ("111111", 13),
])
def test_num_decodings(s, expected):
    assert Solution().numDecodings(s) == expected

