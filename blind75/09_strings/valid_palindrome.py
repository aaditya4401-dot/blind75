"""
Valid Palindrome  |  LeetCode 125  |  Easy
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after lowercasing and removing every non
alphanumeric character, it reads the same forwards and backwards. Return
whether `s` is a palindrome.

Example 1:
    Input:  s = "A man, a plan, a canal: Panama"
    Output: True                # "amanaplanacanalpanama"

Example 2:
    Input:  s = "race a car"
    Output: False

Example 3:
    Input:  s = " "
    Output: True                # the empty string is a palindrome

Constraints:
    1 <= len(s) <= 2 * 10^5
    s is printable ASCII.

Hint:
    Building a filtered copy and comparing it to its reverse is the one-liner.
    For O(1) space, walk two pointers inward and skip non-alphanumerics in place
    -- str.isalnum() and str.lower() are the tools.

Target complexity: O(n) time, O(1) space
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pass
