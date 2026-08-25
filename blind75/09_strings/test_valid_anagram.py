"""Tests for Valid Anagram. Run: pytest 09_strings/test_valid_anagram.py"""
import pytest

from valid_anagram import Solution

@pytest.mark.parametrize("s, t, expected", [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("a", "a", True),
    ("ab", "a", False),
    ("aacc", "ccac", False),
    ("listen", "silent", True),
    ("aabbcc", "abcabc", True),
])
def test_is_anagram(s, t, expected):
    assert Solution().isAnagram(s, t) is expected

