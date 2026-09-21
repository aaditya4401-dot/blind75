"""
Task Scheduler  |  LeetCode 621  |  Medium
https://leetcode.com/problems/task-scheduler/

Given a list of CPU tasks `tasks` (each an uppercase letter) and a cooldown
`n`, where the same task must be separated by at least n intervals, return the
minimum number of CPU intervals needed to finish all tasks (idle intervals
allowed).

Example 1:
    Input:  tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8   # A B idle A B idle A B

Example 2:
    Input:  tasks = ["A","A","A","B","B","B"], n = 0
    Output: 6   # no cooldown needed

Example 3:
    Input:  tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
    Output: 16

Constraints:
    1 <= len(tasks) <= 10^4
    tasks[i] is an uppercase English letter.
    0 <= n <= 100

Hint:
    Two equivalent approaches:

    Math formula: let max_count be the highest frequency of any task, and
    max_count_ties the number of tasks sharing that frequency. The answer is
    max(len(tasks), (max_count - 1) * (n + 1) + max_count_ties) -- the first
    term covers the case where there are enough distinct tasks to fill every
    gap with no idling.

    Simulation: max-heap by count, pop the most frequent tasks into each round
    of size n+1, decrement, push back what's left, count idle slots when the
    heap empties early.

Target complexity: O(n) time for the formula, O(26) space
"""

from typing import List

from collections import deque, Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pass
        count = Counter(tasks)

        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        q = deque()
        time = 0
        while q or maxheap:
            time +=1

            if maxheap:
                cnt = heapq.heappop(maxheap)+1
                if cnt<0:
                    q.append([cnt, time+n])

            if q and q[0][1]==time:
                curr = q.popleft()[0]

                heapq.heappush(maxheap,curr)

        return time

if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
