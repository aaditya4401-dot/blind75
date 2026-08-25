"""Tests for Climbing Stairs. Run: pytest 03_dynamic_programming/test_climbing_stairs.py"""
import pytest

from climbing_stairs import Solution

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (10, 89),
    (45, 1836311903),
])
def test_climb_stairs(n, expected):
    assert Solution().climbStairs(n) == expected

