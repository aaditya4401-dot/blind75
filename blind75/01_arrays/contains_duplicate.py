"""
Contains Duplicate  |  LeetCode 217  |  Easy
https://leetcode.com/problems/contains-duplicate/

Return True if any value appears at least twice in `nums`, and False if every
element is distinct.

Example 1:
    Input:  nums = [1, 2, 3, 1]
    Output: True

Example 2:
    Input:  nums = [1, 2, 3, 4]
    Output: False

Constraints:
    1 <= len(nums) <= 10^5
    -10^9 <= nums[i] <= 10^9

Hint:
    A set of seen values, or compare len(set(nums)) with len(nums). Sorting first
    also works at O(n log n) with O(1) extra space -- know both trade-offs.

Target complexity: O(n) time, O(n) space
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
