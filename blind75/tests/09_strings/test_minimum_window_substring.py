"""Tests for Minimum Window Substring. Run: pytest 09_strings/test_minimum_window_substring.py"""
import pytest

from minimum_window_substring import Solution

@pytest.mark.parametrize("s, t, expected", [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("ab", "b", "b"),
    ("aa", "aa", "aa"),
    ("bba", "ab", "ba"),
    ("cabwefgewcwaefgcf", "cae", "cwae"),
    ("abc", "d", ""),
])
def test_min_window(s, t, expected):
    assert Solution().minWindow(s, t) == expected

