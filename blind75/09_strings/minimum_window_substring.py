"""
Minimum Window Substring  |  LeetCode 76  |  Hard
https://leetcode.com/problems/minimum-window-substring/

Given strings `s` and `t`, return the shortest substring of `s` that contains
every character of `t` including duplicates. If there is none, return "".

Example 1:
    Input:  s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"

Example 2:
    Input:  s = "a", t = "aa"
    Output: ""                  # only one 'a' available

Constraints:
    1 <= len(s), len(t) <= 10^5
    The answer is guaranteed to be unique.

Hint:
    Expanding/contracting sliding window. Count what t needs, then grow `right`
    until the window is complete, and shrink `left` as far as it can go while
    staying complete, recording the best window each time.

    Track a `have`/`need` counter of *satisfied character types* rather than
    re-comparing whole dicts -- that is what keeps it linear.

Target complexity: O(n + m) time, O(alphabet) space
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass
