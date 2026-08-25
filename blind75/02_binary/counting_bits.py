"""
Counting Bits  |  LeetCode 338  |  Easy
https://leetcode.com/problems/counting-bits/

Given an integer `n`, return an array `ans` of length n + 1 where `ans[i]` is
the number of 1 bits in the binary representation of i.

Example 1:
    Input:  n = 2
    Output: [0, 1, 1]           # 0, 1, 10

Example 2:
    Input:  n = 5
    Output: [0, 1, 1, 2, 1, 2]  # 0, 1, 10, 11, 100, 101

Constraints:
    0 <= n <= 10^5

Hint:
    Reuse the answers you already computed -- this is DP, not bit twiddling.
    i >> 1 is i with its last bit dropped, so ans[i] = ans[i >> 1] + (i & 1).
    (The alternative recurrence ans[i] = ans[i & (i - 1)] + 1 works too.)

Target complexity: O(n) time, O(n) space
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_counting_bits.py"))]))
