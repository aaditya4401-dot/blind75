"""Tests for Longest Palindromic Substring. Run: pytest 09_strings/test_longest_palindromic_substring.py"""
import pytest

from longest_palindromic_substring import Solution

@pytest.mark.parametrize("s, accepted", [
    ("babad", {"bab", "aba"}),
    ("cbbd", {"bb"}),
    ("a", {"a"}),
    ("ac", {"a", "c"}),
    ("aaaa", {"aaaa"}),
    ("racecar", {"racecar"}),
    ("abcda", {"a", "b", "c", "d"}),
    ("forgeeksskeegfor", {"geeksskeeg"}),
])
def test_longest_palindrome(s, accepted):
    assert Solution().longestPalindrome(s) in accepted

