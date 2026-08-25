"""
Reverse Bits  |  LeetCode 190  |  Easy
https://leetcode.com/problems/reverse-bits/

Reverse the bits of a given 32-bit unsigned integer.

Example 1:
    Input:  n = 43261596        # 00000010100101000001111010011100
    Output: 964176192           # 00111001011110000010100101000000

Example 2:
    Input:  n = 4294967293      # 11111111111111111111111111111101
    Output: 3221225471          # 10111111111111111111111111111111

Constraints:
    The input is a 32-bit unsigned integer.

Hint:
    Loop 32 times: shift the result left by one, OR in n's lowest bit, then
    shift n right by one. Do all 32 iterations even after n hits 0 -- the
    remaining zero bits still have to be shifted into place.

Target complexity: O(1) time (32 iterations), O(1) space
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        pass
