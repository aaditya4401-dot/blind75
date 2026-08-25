"""
Top K Frequent Elements  |  LeetCode 347  |  Medium
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array `nums` and an integer `k`, return the k most frequent
elements. The answer may be returned in any order.

Example 1:
    Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]

Example 2:
    Input:  nums = [1], k = 1
    Output: [1]

Constraints:
    1 <= len(nums) <= 10^5
    k is in [1, number of distinct elements]
    The answer is guaranteed to be unique.

Hint:
    Count with a dict (or Counter), then pick the top k.

    Heap: keep a size-k min-heap of (count, value) -- O(n log k).

    Bucket sort: index buckets by frequency, since no frequency can exceed
    len(nums). Walk the buckets from the back for a true O(n).

Target complexity: O(n log k) with a heap, or O(n) with bucket sort
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
