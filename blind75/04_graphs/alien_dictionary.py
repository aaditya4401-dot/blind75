"""
Alien Dictionary  |  LeetCode 269  |  Hard
https://leetcode.com/problems/alien-dictionary/

[LeetCode Premium] A new alien language uses lowercase English letters in an
unknown order. Given a list of words sorted lexicographically in that language,
return a string of the letters in the alien order. If the ordering is invalid
return "". Any valid ordering is accepted.

Example 1:
    Input:  words = ["wrt", "wrf", "er", "ett", "rftt"]
    Output: "wertf"

Example 2:
    Input:  words = ["z", "x", "z"]
    Output: ""                  # contradictory

Constraints:
    1 <= len(words) <= 100
    Words are lowercase English letters.

Hint:
    Topological sort. Compare each adjacent pair of words, find the first
    position where they differ, and that gives one edge first_char -> second.
    Stop after the first difference -- later characters tell you nothing.

    Two traps: (1) every letter that appears anywhere must end up in the output,
    even letters with no edges; (2) ["abc", "ab"] is invalid input -- a prefix
    must not follow its longer word -- and must return "".

Target complexity: O(total characters) time, O(1) space (26 letters)
"""

from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        pass
