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
        adj = {}
        for word in words:
            for char in word:
                adj[char] = set()
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minLen]==w2:
                return ""
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        for c in adj:
            visited[c]=0

        result = []

        def dfs(char):
            visited[char]=1
            for nb in adj[char]:
                if visited[nb]==1:
                    return False
                if visited[nb]==0 and not dfs(nb):
                    return False
            visited[char]=2
            result.append(char)
            return True

        for c in adj:
            if visited[c]==0:
                if not dfs(c):
                    return ""

        return "".join(result[::-1])


        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
