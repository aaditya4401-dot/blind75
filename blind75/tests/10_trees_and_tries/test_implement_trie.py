"""Tests for Implement Trie (Prefix Tree). Run: pytest 10_trees_and_tries/test_implement_trie.py"""
import pytest


from implement_trie import Trie


def test_leetcode_example():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True


def test_empty_trie():
    trie = Trie()
    assert trie.search("a") is False
    assert trie.startsWith("a") is False


def test_shared_prefixes():
    trie = Trie()
    for word in ["car", "card", "care", "dog"]:
        trie.insert(word)
    assert trie.search("car") is True
    assert trie.search("care") is True
    assert trie.search("ca") is False
    assert trie.startsWith("ca") is True
    assert trie.startsWith("do") is True
    assert trie.startsWith("dot") is False
    assert trie.search("cards") is False


def test_reinsert_is_idempotent():
    trie = Trie()
    trie.insert("hello")
    trie.insert("hello")
    assert trie.search("hello") is True

