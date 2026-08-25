"""
Find Minimum in Rotated Sorted Array  |  LeetCode 153  |  Medium
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

A sorted array of unique elements was rotated between 1 and n times. Return the
minimum element, in O(log n) time.

Example 1:
    Input:  nums = [3, 4, 5, 1, 2]
    Output: 1                   # original [1,2,3,4,5] rotated 3 times

Example 2:
    Input:  nums = [4, 5, 6, 7, 0, 1, 2]
    Output: 0

Constraints:
    1 <= len(nums) <= 5000
    All values are unique.

Hint:
    Binary search on the shape, not on a target. Compare nums[mid] with
    nums[hi]: if nums[mid] > nums[hi] the pivot is strictly right of mid
    (lo = mid + 1); otherwise mid could still be the minimum (hi = mid).

Target complexity: O(log n) time, O(1) space
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums)-1

        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[l]



if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
