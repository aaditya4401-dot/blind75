"""Tests for Encode and Decode Strings. Run: pytest 09_strings/test_encode_and_decode_strings.py"""
import pytest

from encode_and_decode_strings import Solution

@pytest.mark.parametrize("strs", [
    ["lint", "code", "love", "you"],
    ["hello", "world"],
    [],
    [""],
    ["", ""],
    ["#", "3#abc", ""],
    ["a#b", "##", "1#"],
    ["with space", "with\nnewline", "tab\there"],
    ["12345", "0"],
])
def test_round_trip(strs):
    solution = Solution()
    encoded = solution.encode(strs)
    assert isinstance(encoded, str)
    assert solution.decode(encoded) == strs

