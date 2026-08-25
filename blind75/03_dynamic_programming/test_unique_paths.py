"""Tests for Unique Paths. Run: pytest 03_dynamic_programming/test_unique_paths.py"""
import pytest

from unique_paths import Solution

@pytest.mark.parametrize("m, n, expected", [
    (3, 7, 28),
    (3, 2, 3),
    (1, 1, 1),
    (1, 10, 1),
    (10, 1, 1),
    (2, 2, 2),
    (7, 3, 28),
    (10, 10, 48620),
])
def test_unique_paths(m, n, expected):
    assert Solution().uniquePaths(m, n) == expected

