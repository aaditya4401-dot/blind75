"""Tests for Serialize and Deserialize Binary Tree. Run: pytest 10_trees_and_tries/test_serialize_and_deserialize_binary_tree.py"""
import pytest

from common.structures import build_tree, tree_to_list

from serialize_and_deserialize_binary_tree import Codec


@pytest.mark.parametrize("values", [
    [1, 2, 3, None, None, 4, 5],
    [],
    [1],
    [1, 2],
    [1, None, 2],
    [5, 2, 3, None, None, 2, 4, 3, 1],
    [-1, -2, -3],
    [1, 2, 3, 4, 5, 6, 7],
])
def test_round_trip(values):
    codec = Codec()
    data = codec.serialize(build_tree(values))
    assert isinstance(data, str)
    assert tree_to_list(codec.deserialize(data)) == values

