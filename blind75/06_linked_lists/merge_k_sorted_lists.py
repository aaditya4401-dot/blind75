"""
Merge k Sorted Lists  |  LeetCode 23  |  Hard
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k sorted linked lists. Merge them into one sorted
list and return it.

Example 1:
    Input:  lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    Output: [1, 1, 2, 3, 4, 4, 5, 6]

Example 2:
    Input:  lists = []
    Output: []

Constraints:
    0 <= k <= 10^4
    The total number of nodes across all lists is at most 10^4.

Hint:
    Two good answers, both O(N log k):

    Min-heap -- push the head of each list, pop the smallest, append it, push
    its successor. In Python push tuples (val, index, node); the index breaks
    ties because ListNode has no ordering.

    Divide and conquer -- pair the lists up and mergeTwoLists each pair, halving
    k each round. No heap needed, and it reuses problem 21.

    (This problem is listed under both Linked List and Heap in Blind 75.)

Target complexity: O(N log k) time, O(k) space
"""

from typing import List, Optional

from common.structures import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_merge_k_sorted_lists.py"))]))
