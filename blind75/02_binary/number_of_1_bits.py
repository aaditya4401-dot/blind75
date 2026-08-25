"""
Number of 1 Bits  |  LeetCode 191  |  Easy
https://leetcode.com/problems/number-of-1-bits/

Return the number of set bits (the Hamming weight) in the binary representation
of a positive integer `n`.

Example 1:
    Input:  n = 11              # 0b1011
    Output: 3

Example 2:
    Input:  n = 128             # 0b10000000
    Output: 1

Constraints:
    1 <= n <= 2^31 - 1

Hint:
    The obvious loop shifts right 32 times counting n & 1. The sharper trick is
    n &= n - 1, which clears the lowest set bit each pass -- so the loop runs
    once per set bit instead of once per bit.

Target complexity: O(number of set bits) time, O(1) space
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
