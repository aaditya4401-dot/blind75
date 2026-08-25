"""Tests for Palindromic Substrings. Run: pytest 09_strings/test_palindromic_substrings.py"""
import pytest

from palindromic_substrings import Solution

@pytest.mark.parametrize("s, expected", [
    ("abc", 3),
    ("aaa", 6),
    ("a", 1),
    ("aa", 3),
    ("abba", 6),
    ("racecar", 10),
    ("abab", 6),
])
def test_count_substrings(s, expected):
    assert Solution().countSubstrings(s) == expected

