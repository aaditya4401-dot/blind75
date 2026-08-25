"""
Sum of Two Integers  |  LeetCode 371  |  Medium
https://leetcode.com/problems/sum-of-two-integers/

Return the sum of two integers `a` and `b` without using the operators + or -.

Example 1:
    Input:  a = 1, b = 2
    Output: 3

Example 2:
    Input:  a = 2, b = 3
    Output: 5

Constraints:
    -1000 <= a, b <= 1000

Hint:
    a ^ b adds bit-by-bit while ignoring carries; (a & b) << 1 is exactly the
    carries. Loop until there is no carry left.

    Python trap: its ints are arbitrary precision, so negatives never "wrap".
    Mask with 0xFFFFFFFF each iteration, and at the end, if the result has bit
    31 set, convert it back to a negative via ~(result ^ 0xFFFFFFFF).

Target complexity: O(1) time (fixed 32-bit width), O(1) space
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_sum_of_two_integers.py"))]))
