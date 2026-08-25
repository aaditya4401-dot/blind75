"""
Course Schedule  |  LeetCode 207  |  Medium
https://leetcode.com/problems/course-schedule/

There are `numCourses` courses labelled 0..numCourses-1. `prerequisites[i] =
[a, b]` means you must take b before a. Return True if you can finish all
courses.

Example 1:
    Input:  numCourses = 2, prerequisites = [[1, 0]]
    Output: True

Example 2:
    Input:  numCourses = 2, prerequisites = [[1, 0], [0, 1]]
    Output: False               # a cycle

Constraints:
    1 <= numCourses <= 2000
    0 <= len(prerequisites) <= 5000
    All prerequisite pairs are distinct.

Hint:
    This is "does this directed graph have a cycle". Two standard answers:

    Kahn's BFS -- compute in-degrees, queue every zero-in-degree node, peel them
    off decrementing neighbors; if you processed fewer than numCourses nodes, a
    cycle remains.

    DFS with three colors -- unvisited / in-progress / done. Hitting an
    in-progress node means a cycle. A plain boolean visited set is not enough.

Target complexity: O(V + E) time, O(V + E) space
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
