"""Tests for Longest Repeating Character Replacement. Run: pytest 09_strings/test_longest_repeating_character_replacement.py"""
import pytest

from longest_repeating_character_replacement import Solution

@pytest.mark.parametrize("s, k, expected", [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),
    ("A", 0, 1),
    ("AAAA", 0, 4),
    ("ABCDE", 0, 1),
    ("ABBB", 2, 4),
    ("AAAB", 0, 3),
    ("ABAA", 0, 2),
])
def test_character_replacement(s, k, expected):
    assert Solution().characterReplacement(s, k) == expected

