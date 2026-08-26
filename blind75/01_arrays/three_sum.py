"""
3Sum  |  LeetCode 15  |  Medium
https://leetcode.com/problems/3sum/

Return all unique triplets [nums[i], nums[j], nums[k]] with distinct indices
such that they sum to 0. The solution set must not contain duplicate triplets.

Example 1:
    Input:  nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

Example 2:
    Input:  nums = [0, 1, 1]
    Output: []

Constraints:
    3 <= len(nums) <= 3000
    -10^5 <= nums[i] <= 10^5

Hint:
    Sort first. Fix nums[i], then two-pointer the remaining suffix for a pair
    summing to -nums[i]. Sorting is what makes dedup cheap: skip nums[i] when it
    equals nums[i-1], and after recording a hit advance both pointers past
    their duplicates.

Target complexity: O(n^2) time, O(1) extra space (sorting aside)
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()
        result = []
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue

            l = i+1
            r = n-1

            while l<r:
                total = nums[i]+nums[l]+nums[r]

                if total ==0:
                    result.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1

                    while l<r and nums[r]==nums[r-1]:
                        r-=1

                    l+=1
                    r-=1

                elif total<0:
                    l+=1
                else:
                    r-=1
        return result

        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
