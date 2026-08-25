"""
Maximum Product Subarray  |  LeetCode 152  |  Medium
https://leetcode.com/problems/maximum-product-subarray/

Find the contiguous subarray with the largest product and return that product.

Example 1:
    Input:  nums = [2, 3, -2, 4]
    Output: 6                   # the subarray [2, 3]

Example 2:
    Input:  nums = [-2, 0, -1]
    Output: 0                   # [-2, -1] is not contiguous

Constraints:
    1 <= len(nums) <= 2 * 10^4
    -10 <= nums[i] <= 10
    Every prefix product fits in a 32-bit integer.

Hint:
    Kadane's, but a negative number flips largest into smallest. Track BOTH the
    max product and the min product ending at i, and swap them when nums[i] < 0.
    A zero resets both to nums[i].

Target complexity: O(n) time, O(1) space
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_maximum_product_subarray.py"))]))
