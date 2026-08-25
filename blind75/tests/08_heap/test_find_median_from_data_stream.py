"""Tests for Find Median from Data Stream. Run: pytest 08_heap/test_find_median_from_data_stream.py"""
import pytest


import random
import statistics

from find_median_from_data_stream import MedianFinder


def test_basic_flow():
    mf = MedianFinder()
    mf.addNum(1)
    assert mf.findMedian() == 1.0
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0


def test_negatives_and_duplicates():
    mf = MedianFinder()
    for n in [-1, -2, -3, -4, -5]:
        mf.addNum(n)
    assert mf.findMedian() == -3.0

    mf = MedianFinder()
    for n in [6, 6, 6, 6]:
        mf.addNum(n)
    assert mf.findMedian() == 6.0


def test_matches_statistics_median():
    random.seed(75)
    mf, seen = MedianFinder(), []
    for _ in range(200):
        n = random.randint(-100, 100)
        mf.addNum(n)
        seen.append(n)
        assert mf.findMedian() == pytest.approx(statistics.median(seen))

