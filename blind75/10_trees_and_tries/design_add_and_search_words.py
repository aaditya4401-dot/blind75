"""
Design Add and Search Words Data Structure  |  LeetCode 211  |  Medium
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a structure supporting:
    addWord(word)   -- add word to the structure
    search(word)    -- True if any added word matches; word may contain '.',
                       which matches any single character

Example:
    d.addWord("bad"); d.addWord("dad"); d.addWord("mad")
    d.search("pad")   -> False
    d.search("bad")   -> True
    d.search(".ad")   -> True
    d.search("b..")   -> True

Constraints:
    1 <= len(word) <= 25
    Lowercase letters, plus '.' in search queries.
    Up to 10^4 calls.

Hint:
    A trie again, but search becomes a DFS: on a normal character follow that
    one child; on '.' recurse into EVERY child and succeed if any branch does.
    Compare with Implement Trie -- the only change is the wildcard branch.

Target complexity: O(len(word)) to add; O(26^d * len(word)) worst case to search with dots
"""

class WordDictionary:
    def __init__(self):
        pass

    def addWord(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
