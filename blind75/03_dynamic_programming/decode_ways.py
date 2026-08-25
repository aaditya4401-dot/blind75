"""
Decode Ways  |  LeetCode 91  |  Medium
https://leetcode.com/problems/decode-ways/

'A' maps to "1" ... 'Z' maps to "26". Given a digit string `s`, return the
number of ways to decode it. The mapping is only ever applied to the groupings
"1".."26"; a leading zero is never valid ("06" is not "F").

Example 1:
    Input:  s = "12"
    Output: 2                   # "AB" (1 2) or "L" (12)

Example 2:
    Input:  s = "226"
    Output: 3                   # "BZ", "VF", "BBF"

Example 3:
    Input:  s = "06"
    Output: 0

Constraints:
    1 <= len(s) <= 100
    s contains only digits.

Hint:
    Fibonacci-shaped with validity gates. dp[i] = (dp[i-1] if s[i-1] != "0") +
    (dp[i-2] if 10 <= int(s[i-2:i]) <= 26). All the difficulty here is zeros:
    a "0" can only survive as the second digit of 10 or 20.

Target complexity: O(n) time, O(1) space
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_decode_ways.py"))]))
