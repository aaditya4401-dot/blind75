"""Data structures and helpers shared across the Blind 75 problems.

LeetCode hands you bare `ListNode` / `TreeNode` / `Node` classes and feeds them
serialized input. These helpers let the tests do the same thing locally: build a
structure from a plain Python list, and read one back out for comparison.
"""

from collections import deque
from typing import List, Optional


# --------------------------------------------------------------------------- #
# Linked list
# --------------------------------------------------------------------------- #
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        vals, node, seen = [], self, set()
        while node and id(node) not in seen:
            seen.add(id(node))
            vals.append(str(node.val))
            node = node.next
        if node:
            vals.append("...cycle")
        return "ListNode(" + " -> ".join(vals) + ")"


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    """[1, 2, 3] -> 1 -> 2 -> 3 -> None"""
    head = None
    for val in reversed(values):
        head = ListNode(val, head)
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """1 -> 2 -> 3 -> None  ->  [1, 2, 3]"""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def build_cyclic_list(values: List[int], pos: int) -> Optional[ListNode]:
    """Build a list whose tail points back at index `pos` (-1 for no cycle)."""
    head = build_linked_list(values)
    if head is None:
        return None
    nodes, node = [], head
    while node:
        nodes.append(node)
        node = node.next
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return head


def node_at(head: Optional[ListNode], index: int) -> Optional[ListNode]:
    """Return the node sitting at `index`, or None if the list is shorter."""
    for _ in range(index):
        if head is None:
            return None
        head = head.next
    return head


# --------------------------------------------------------------------------- #
# Binary tree
# --------------------------------------------------------------------------- #
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "TreeNode(%r)" % (tree_to_list(self),)


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """LeetCode level-order format: [3, 9, 20, None, None, 15, 7].

    `None` marks a missing child and its slot is *not* expanded further, which
    is exactly how LeetCode's own serialization works.
    """
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Inverse of build_tree, with trailing Nones trimmed."""
    if root is None:
        return []
    out, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Locate the node holding `val` (values are unique in these problems)."""
    if root is None:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


# --------------------------------------------------------------------------- #
# Graph node (Clone Graph)
# --------------------------------------------------------------------------- #
class GraphNode:
    """LeetCode calls this `Node`; renamed here so imports stay readable."""

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return "GraphNode(%d)" % self.val


def build_graph(adj: List[List[int]]) -> Optional[GraphNode]:
    """adj is 1-indexed as LeetCode gives it: adj[i] are node (i+1)'s neighbors."""
    if not adj:
        return None
    nodes = {i + 1: GraphNode(i + 1) for i in range(len(adj))}
    for i, neighbors in enumerate(adj):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def graph_to_adj(node: Optional[GraphNode]) -> List[List[int]]:
    """Serialize a graph back to the 1-indexed adjacency list."""
    if node is None:
        return []
    seen, stack = {}, [node]
    while stack:
        cur = stack.pop()
        if cur.val in seen:
            continue
        seen[cur.val] = cur
        stack.extend(cur.neighbors)
    return [sorted(n.val for n in seen[v].neighbors) for v in sorted(seen)]
