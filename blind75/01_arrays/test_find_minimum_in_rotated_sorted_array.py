"""Tests for Find Minimum in Rotated Sorted Array. Run: pytest 01_arrays/test_find_minimum_in_rotated_sorted_array.py"""
import pytest

from find_minimum_in_rotated_sorted_array import Solution

@pytest.mark.parametrize("nums, expected", [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([11, 13, 15, 17], 11),
    ([1], 1),
    ([2, 1], 1),
    ([5, 1, 2, 3, 4], 1),
    # The minimum sitting exactly at or just past mid -- catches the classic
    # off-by-one where `hi = mid - 1` discards mid while mid IS the answer.
    ([2, 0, 1], 0),
    ([3, 4, 5, 0, 1, 2], 0),
    ([2, 3, 4, 5, 0, 1], 0),
    ([4, 5, 6, 0, 1, 2, 3], 0),
    ([3, 1, 2], 1),
])
def test_find_min(nums, expected):
    assert Solution().findMin(nums) == expected


def test_every_rotation_of_every_size():
    """Exhaustive: every rotation of every distinct sorted array up to length 12.

    Binary search on a rotated array has a lot of near-miss variants that pass a
    handful of hand-picked cases, so this checks all 78 of them.
    """
    for n in range(1, 13):
        base = list(range(n))
        for k in range(n):
            rotated = base[k:] + base[:k]
            assert Solution().findMin(list(rotated)) == 0, "failed on %r" % (rotated,)


def test_negative_and_sparse_values():
    """Values need not be contiguous, and may be negative."""
    for nums, expected in [
        ([-4, -1, 7, 9, -9, -7, -5], -9),
        ([30, 40, 50, 10, 20], 10),
        ([-1], -1),
        ([0, -1], -1),
    ]:
        assert Solution().findMin(nums) == expected

