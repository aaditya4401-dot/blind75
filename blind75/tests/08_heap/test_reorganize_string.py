"""Tests for Reorganize String. Run: pytest 08_heap/test_reorganize_string.py"""
from collections import Counter

import pytest


from reorganize_string import Solution


def _is_valid_reorganization(original: str, result: str) -> bool:
    if Counter(original) != Counter(result):
        return False
    return all(result[i] != result[i + 1] for i in range(len(result) - 1))


@pytest.mark.parametrize("s", ["aab", "vvvlo", "aabbcc"])
def test_produces_valid_arrangement(s):
    result = Solution().reorganizeString(s)
    assert _is_valid_reorganization(s, result)


def test_impossible_case():
    assert Solution().reorganizeString("aaab") == ""


def test_single_character():
    assert Solution().reorganizeString("a") == "a"


def test_already_alternating():
    result = Solution().reorganizeString("ab")
    assert _is_valid_reorganization("ab", result)
