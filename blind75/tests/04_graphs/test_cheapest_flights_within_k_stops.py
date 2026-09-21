"""Tests for Cheapest Flights Within K Stops. Run: pytest 04_graphs/test_cheapest_flights_within_k_stops.py"""
import pytest


from cheapest_flights_within_k_stops import Solution


@pytest.mark.parametrize(
    "n, flights, src, dst, k, expected",
    [
        (
            4,
            [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            0,
            3,
            1,
            700,
        ),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
    ],
)
def test_cheapest_flights(n, flights, src, dst, k, expected):
    assert Solution().findCheapestPrice(n, flights, src, dst, k) == expected


def test_no_route_exists():
    assert Solution().findCheapestPrice(3, [[0, 1, 100]], 0, 2, 1) == -1


def test_not_enough_stops():
    flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100]]
    assert Solution().findCheapestPrice(4, flights, 0, 3, 1) == -1
