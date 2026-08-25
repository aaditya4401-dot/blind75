"""Tests for Longest Common Subsequence. Run: pytest 03_dynamic_programming/test_longest_common_subsequence.py"""
import pytest

from longest_common_subsequence import Solution

@pytest.mark.parametrize("text1, text2, expected", [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0),
    ("a", "a", 1),
    ("bsbininm", "jmjkbkjkv", 1),
    ("oxcpqrsvwf", "shmtulqrypy", 2),
    ("abcba", "abcbcba", 5),
])
def test_lcs(text1, text2, expected):
    assert Solution().longestCommonSubsequence(text1, text2) == expected

