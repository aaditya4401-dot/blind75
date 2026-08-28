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
        n = len(s)
        
        dp = [-1]*(n+1)
        return self.helper(n,s,dp)
    def helper(self, ind, s, dp):
        
        if ind==0:
            return 1
        
        if dp[ind]!=-1:
            return dp[ind]
        
        ans1 ,ans2 = 0 , 0
        if s[ind-1]!="0":
            ans1 = self.helper(ind-1,s,dp)
        if ind>=2 and 10<= int(s[ind-2:ind])<=26:
            ans2 = self.helper(ind-2,s,dp)
        
        dp[ind] = ans1 + ans2

        return dp[ind]
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
