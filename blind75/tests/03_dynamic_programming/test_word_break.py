"""Tests for Word Break. Run: pytest 03_dynamic_programming/test_word_break.py"""
import pytest

from word_break import Solution

@pytest.mark.parametrize("s, word_dict, expected", [
    ("leetcode", ["leet", "code"], True),
    ("applepenapple", ["apple", "pen"], True),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ("a", ["a"], True),
    ("a", ["b"], False),
    ("cars", ["car", "ca", "rs"], True),
    ("aaaaaaa", ["aaaa", "aaa"], True),
    ("abcd", ["a", "abc", "b", "cd"], True),
])
def test_word_break(s, word_dict, expected):
    assert Solution().wordBreak(s, word_dict) is expected

