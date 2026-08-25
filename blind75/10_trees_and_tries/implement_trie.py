"""
Implement Trie (Prefix Tree)  |  LeetCode 208  |  Medium
https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with:
    insert(word)        -- insert word into the trie
    search(word)        -- True if word was inserted
    startsWith(prefix)  -- True if any inserted word starts with prefix

Example:
    trie.insert("apple")
    trie.search("apple")      -> True
    trie.search("app")        -> False
    trie.startsWith("app")    -> True
    trie.insert("app")
    trie.search("app")        -> True

Constraints:
    1 <= len(word), len(prefix) <= 2000
    Lowercase English letters only.
    Up to 3 * 10^4 calls total.

Hint:
    Each node holds a dict child_char -> node plus an is_end flag. That flag is
    the entire difference between search and startsWith: both walk the same
    path, but search additionally requires is_end at the destination.

Target complexity: O(len(word)) per operation, O(total characters) space
"""

class Trie:
    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass
