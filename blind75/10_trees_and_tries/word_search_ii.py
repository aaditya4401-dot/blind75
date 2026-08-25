"""
Word Search II  |  LeetCode 212  |  Hard
https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of words, return all words from
the list that can be spelled by walking 4-directionally adjacent cells, using
each cell at most once per word.

Example 1:
    Input:  board = [["o","a","a","n"],
                     ["e","t","a","e"],
                     ["i","h","k","r"],
                     ["i","f","l","v"]],
            words = ["oath", "pea", "eat", "rain"]
    Output: ["oath", "eat"]

Constraints:
    1 <= m, n <= 12
    1 <= len(words) <= 3 * 10^4
    1 <= len(words[i]) <= 10

Hint:
    Running Word Search (79) once per word is far too slow. Instead build a trie
    of all the words and DFS the board ONCE, walking the trie in step with the
    path -- the moment a prefix leaves the trie you prune every word sharing it.

    Store the whole word on its terminal node so you can collect matches without
    rebuilding strings. Optimization worth doing: after a word is found, unset
    its marker (and prune childless nodes) so it is not reported twice.

Target complexity: O(m * n * 4^L) time, O(total characters) space
"""

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_word_search_ii.py"))]))
