"""
Merge Two Sorted Lists  |  LeetCode 21  |  Easy
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists into one sorted list, splicing together the
existing nodes. Return the head of the merged list.

Example 1:
    Input:  list1 = [1, 2, 4], list2 = [1, 3, 4]
    Output: [1, 1, 2, 3, 4, 4]

Example 2:
    Input:  list1 = [], list2 = [0]
    Output: [0]

Constraints:
    0 <= number of nodes in each list <= 50
    Both lists are sorted non-decreasing.

Hint:
    A dummy head node removes every "is this the first element" special case.
    Walk both lists appending the smaller node, then attach whichever list still
    has nodes left -- it is already sorted, no need to keep looping.

Target complexity: O(n + m) time, O(1) space
"""

from typing import Optional

from common.structures import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        pass
