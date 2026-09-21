"""Tests for Network Delay Time. Run: pytest 04_graphs/test_network_delay_time.py"""
import pytest


from network_delay_time import Solution


@pytest.mark.parametrize(
    "times, n, k, expected",
    [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[1, 2, 1]], 2, 1, 1),
        ([[1, 2, 1]], 2, 2, -1),
        ([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1, 3),
    ],
)
def test_network_delay_time(times, n, k, expected):
    assert Solution().networkDelayTime(times, n, k) == expected


def test_single_node():
    assert Solution().networkDelayTime([], 1, 1) == 0


def test_unreachable_node():
    assert Solution().networkDelayTime([[1, 2, 1]], 3, 1) == -1
