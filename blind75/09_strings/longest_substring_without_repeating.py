"""
Longest Substring Without Repeating Characters  |  LeetCode 3  |  Medium
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string `s`, return the length of the longest substring without
repeating characters.

Example 1:
    Input:  s = "abcabcbb"
    Output: 3                   # "abc"

Example 2:
    Input:  s = "bbbbb"
    Output: 1                   # "b"

Example 3:
    Input:  s = "pwwkew"
    Output: 3                   # "wke" -- "pwke" is a subsequence, not a substring

Constraints:
    0 <= len(s) <= 5 * 10^4
    s may contain letters, digits, symbols and spaces.

Hint:
    Sliding window. Extend `right`; when the new character is already inside the
    window, pull `left` forward past its previous occurrence. Storing
    char -> last index lets you jump `left` directly instead of shrinking one
    step at a time -- but never let `left` move backwards.

Target complexity: O(n) time, O(min(n, alphabet)) space
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass
