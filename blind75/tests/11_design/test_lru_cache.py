"""Tests for LRU Cache. Run: pytest 11_design/test_lru_cache.py"""
import pytest


from lru_cache import LRUCache


def test_leetcode_example():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_get_missing_key():
    cache = LRUCache(1)
    assert cache.get(1) == -1


def test_put_overwrite_updates_value_and_recency():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)  # updates value, 1 becomes most recent
    cache.put(3, 3)  # evicts key 2 (least recently used)
    assert cache.get(2) == -1
    assert cache.get(1) == 10
    assert cache.get(3) == 3


def test_capacity_one():
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(2) == 2


def test_get_refreshes_recency():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)  # 1 is now most recently used
    cache.put(3, 3)  # evicts key 2, not key 1
    assert cache.get(1) == 1
    assert cache.get(2) == -1
    assert cache.get(3) == 3
