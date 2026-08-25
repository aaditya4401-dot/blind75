"""
Jump Game  |  LeetCode 55  |  Medium
https://leetcode.com/problems/jump-game/

`nums[i]` is the maximum jump length from index i. Starting at index 0, return
True if you can reach the last index.

Example 1:
    Input:  nums = [2, 3, 1, 1, 4]
    Output: True                # 0 -> 1 -> 4

Example 2:
    Input:  nums = [3, 2, 1, 0, 4]
    Output: False               # every route stalls on the 0 at index 3

Constraints:
    1 <= len(nums) <= 10^4
    0 <= nums[i] <= 10^5

Hint:
    Greedy beats DP here. Sweep left to right tracking the furthest index
    reachable so far; if i ever exceeds it you are stuck. Equivalent backwards
    version: keep a `goal` starting at the last index and pull it left whenever
    i + nums[i] >= goal -- you succeed if goal reaches 0.

Target complexity: O(n) time, O(1) space
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
