"""
House Robber  |  LeetCode 198  |  Medium
https://leetcode.com/problems/house-robber/

Each house holds `nums[i]` money, but robbing two adjacent houses trips the
alarm. Return the maximum you can steal.

Example 1:
    Input:  nums = [1, 2, 3, 1]
    Output: 4                   # rob houses 0 and 2

Example 2:
    Input:  nums = [2, 7, 9, 3, 1]
    Output: 12                  # rob houses 0, 2 and 4

Constraints:
    1 <= len(nums) <= 100
    0 <= nums[i] <= 400

Hint:
    At each house the choice is rob it (nums[i] + best up to i-2) or skip it
    (best up to i-1). Take the max. Two rolling variables are enough -- no array
    needed.

Target complexity: O(n) time, O(1) space
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_house_robber.py"))]))
