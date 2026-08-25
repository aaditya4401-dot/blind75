"""Tests for 3Sum. Run: pytest 01_arrays/test_three_sum.py"""
import pytest

from three_sum import Solution

def normalize(triplets):
    return sorted(sorted(t) for t in triplets)


@pytest.mark.parametrize("nums, expected", [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]]),
    ([0, 0, 0, 0], [[0, 0, 0]]),
    ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    ([1, 2, 3], []),
])
def test_three_sum(nums, expected):
    assert normalize(Solution().threeSum(nums)) == normalize(expected)

