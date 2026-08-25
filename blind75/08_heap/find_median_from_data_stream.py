"""
Find Median from Data Stream  |  LeetCode 295  |  Hard
https://leetcode.com/problems/find-median-from-data-stream/

Design a structure supporting a stream of integers:
    addNum(num)   -- add num to the stream
    findMedian()  -- return the median of all elements so far

Example:
    MedianFinder mf
    mf.addNum(1)        # [1]
    mf.addNum(2)        # [1, 2]
    mf.findMedian()     -> 1.5
    mf.addNum(3)        # [1, 2, 3]
    mf.findMedian()     -> 2.0

Constraints:
    -10^5 <= num <= 10^5
    findMedian is only called after at least one addNum.
    Up to 5 * 10^4 calls.

Hint:
    Two heaps straddling the middle: a max-heap for the smaller half, a min-heap
    for the larger half. Python's heapq is min-only, so negate values going into
    the max-heap.

    Keep the sizes within one of each other by rebalancing after every insert.
    The median is then the top of the bigger heap, or the average of the two
    tops when sizes are equal.

Target complexity: O(log n) per addNum, O(1) per findMedian
"""

class MedianFinder:
    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_find_median_from_data_stream.py"))]))
