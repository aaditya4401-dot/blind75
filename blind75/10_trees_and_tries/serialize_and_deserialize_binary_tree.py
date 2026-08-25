"""
Serialize and Deserialize Binary Tree  |  LeetCode 297  |  Hard
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Design an algorithm to serialize a binary tree to a string and deserialize that
string back into the same tree structure.

    codec.deserialize(codec.serialize(root))  must equal  root

Example 1:
    Input:  root = [1, 2, 3, None, None, 4, 5]
    Output: [1, 2, 3, None, None, 4, 5]   (after a round trip)

Example 2:
    Input:  root = []
    Output: []

Constraints:
    0 <= number of nodes <= 10^4
    -1000 <= Node.val <= 1000

Hint:
    The format is yours to choose -- the only requirement is that it round
    trips. Preorder DFS with an explicit null marker is the cleanest: write
    "1,2,#,#,3,..." and rebuild with an iterator, consuming one token per
    recursive call. A "#" means return None.

    Preorder alone is ambiguous; preorder WITH null markers is not -- that is
    why the markers matter. BFS with markers works equally well.

Note: locally `TreeNode` comes from common.structures, and tests build trees
from LeetCode's level-order list format (None marks a missing child).

Target complexity: O(n) time and O(n) space, both directions
"""

from typing import Optional

from common.structures import TreeNode


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encode a tree to a single string."""
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decode your encoded string back to a tree."""
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
