"""
Container With Most Water  |  LeetCode 11  |  Medium
https://leetcode.com/problems/container-with-most-water/

`height[i]` is the height of a vertical line at x = i. Pick two lines that,
together with the x-axis, hold the most water. Return that maximum area.

Example 1:
    Input:  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49                  # lines at index 1 and 8: min(8,7) * (8-1)

Example 2:
    Input:  height = [1, 1]
    Output: 1

Constraints:
    2 <= len(height) <= 10^5
    0 <= height[i] <= 10^4

Hint:
    Two pointers at both ends. Area is min(h[l], h[r]) * (r - l). Moving the
    taller line inward can never help -- width shrinks and the height is still
    capped by the shorter line -- so always move the shorter one.

Target complexity: O(n) time, O(1) space
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_container_with_most_water.py"))]))
