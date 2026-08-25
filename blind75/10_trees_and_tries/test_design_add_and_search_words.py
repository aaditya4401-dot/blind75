"""Tests for Design Add and Search Words Data Structure. Run: pytest 10_trees_and_tries/test_design_add_and_search_words.py"""
import pytest


from design_add_and_search_words import WordDictionary


def test_leetcode_example():
    d = WordDictionary()
    d.addWord("bad")
    d.addWord("dad")
    d.addWord("mad")
    assert d.search("pad") is False
    assert d.search("bad") is True
    assert d.search(".ad") is True
    assert d.search("b..") is True


def test_wildcards_and_lengths():
    d = WordDictionary()
    d.addWord("a")
    d.addWord("ab")
    assert d.search("a") is True
    assert d.search("a.") is True
    assert d.search("ab") is True
    assert d.search(".a") is False
    assert d.search(".b") is True
    assert d.search("ab.") is False
    assert d.search(".") is True
    assert d.search("..") is True


def test_all_dots_on_empty():
    d = WordDictionary()
    assert d.search(".") is False
    d.addWord("xyz")
    assert d.search("...") is True
    assert d.search("....") is False

