"""Tests for Word Search. Run: pytest 07_matrix/test_word_search.py"""
import pytest

from word_search import Solution

BOARD = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]


@pytest.mark.parametrize("board, word, expected", [
    ([r[:] for r in BOARD], "ABCCED", True),
    ([r[:] for r in BOARD], "SEE", True),
    ([r[:] for r in BOARD], "ABCB", False),
    ([["A"]], "A", True),
    ([["A"]], "B", False),
    ([["A", "B"], ["C", "D"]], "ABDC", True),
    ([["A", "B"], ["C", "D"]], "ABCD", False),
    ([["a", "a"]], "aaa", False),
])
def test_exist(board, word, expected):
    assert Solution().exist(board, word) is expected

