"""
Product of Array Except Self  |  LeetCode 238  |  Medium
https://leetcode.com/problems/product-of-array-except-self/

Return an array `answer` where `answer[i]` is the product of every element of
`nums` except `nums[i]`.

You must solve it without using division, and in O(n) time.

Example 1:
    Input:  nums = [1, 2, 3, 4]
    Output: [24, 12, 8, 6]

Example 2:
    Input:  nums = [-1, 1, 0, -3, 3]
    Output: [0, 0, 9, 0, 0]

Constraints:
    2 <= len(nums) <= 10^5
    The product of any prefix or suffix fits in a 32-bit integer.

Hint:
    answer[i] = (product of everything left of i) * (product of everything right
    of i). Do a left-to-right pass filling answer with prefix products, then a
    right-to-left pass multiplying in a running suffix product. Zeros then need
    no special-casing.

Target complexity: O(n) time, O(1) extra space (output array excluded)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
