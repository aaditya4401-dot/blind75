"""Tests for Group Anagrams. Run: pytest 09_strings/test_group_anagrams.py"""
import pytest

from group_anagrams import Solution

def normalize(groups):
    return sorted(sorted(g) for g in groups)


@pytest.mark.parametrize("strs, expected", [
    (["eat", "tea", "tan", "ate", "nat", "bat"],
     [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    ([""], [[""]]),
    (["a"], [["a"]]),
    (["", ""], [["", ""]]),
    (["abc", "bca", "cab", "xyz"], [["abc", "bca", "cab"], ["xyz"]]),
    (["ab", "ba", "abc"], [["ab", "ba"], ["abc"]]),
])
def test_group_anagrams(strs, expected):
    assert normalize(Solution().groupAnagrams(strs)) == normalize(expected)

