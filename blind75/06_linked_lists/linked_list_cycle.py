"""
Linked List Cycle  |  LeetCode 141  |  Easy
https://leetcode.com/problems/linked-list-cycle/

Return True if the linked list has a cycle in it.

Example 1:
    Input:  head = [3, 2, 0, -4], pos = 1   (tail connects to index 1)
    Output: True

Example 2:
    Input:  head = [1], pos = -1
    Output: False

Constraints:
    0 <= number of nodes <= 10^4
    `pos` is not passed to your function -- it only describes the test input.

Hint:
    Floyd's tortoise and hare: slow moves one node, fast moves two. If there is
    a cycle the fast pointer laps the slow one and they meet; if fast (or
    fast.next) hits None there is no cycle. A visited set works too but costs
    O(n) space.

Target complexity: O(n) time, O(1) space
"""

from typing import Optional

from common.structures import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
