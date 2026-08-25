"""Tests for Word Search II. Run: pytest 10_trees_and_tries/test_word_search_ii.py"""
import pytest

from word_search_ii import Solution

BOARD = [["o", "a", "a", "n"],
         ["e", "t", "a", "e"],
         ["i", "h", "k", "r"],
         ["i", "f", "l", "v"]]


@pytest.mark.parametrize("board, words, expected", [
    ([r[:] for r in BOARD], ["oath", "pea", "eat", "rain"], ["eat", "oath"]),
    ([["a", "b"], ["c", "d"]], ["abcb"], []),
    ([["a"]], ["a"], ["a"]),
    ([["a", "b"]], ["ab", "ba", "a", "b", "c"], ["a", "ab", "b", "ba"]),
    ([["a", "a"]], ["aaa"], []),
    ([r[:] for r in BOARD], [], []),
])
def test_find_words(board, words, expected):
    assert sorted(Solution().findWords(board, words)) == sorted(expected)

