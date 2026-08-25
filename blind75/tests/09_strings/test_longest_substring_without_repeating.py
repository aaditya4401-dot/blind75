"""Tests for Longest Substring Without Repeating Characters. Run: pytest 09_strings/test_longest_substring_without_repeating.py"""
import pytest

from longest_substring_without_repeating import Solution

@pytest.mark.parametrize("s, expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    (" ", 1),
    ("au", 2),
    ("dvdf", 3),
    ("abba", 2),
    ("tmmzuxt", 5),
])
def test_length_of_longest_substring(s, expected):
    assert Solution().lengthOfLongestSubstring(s) == expected

