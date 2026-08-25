"""
Valid Parentheses  |  LeetCode 20  |  Easy
https://leetcode.com/problems/valid-parentheses/

Given a string of just '(', ')', '{', '}', '[' and ']', determine whether it is
valid: every bracket closed by the same type, in the correct order, and every
closing bracket has a matching open one.

Example 1:
    Input:  s = "()[]{}"
    Output: True

Example 2:
    Input:  s = "(]"
    Output: False

Constraints:
    1 <= len(s) <= 10^4

Hint:
    Stack. Push openers; on a closer, the stack top must be its partner -- pop
    it or fail. Two failure modes people forget: a closer with an empty stack,
    and a non-empty stack at the end ("((" is invalid).

Target complexity: O(n) time, O(n) space
"""

class Solution:
    def isValid(self, s: str) -> bool:
        pass
