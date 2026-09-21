"""
LRU Cache  |  LeetCode 146  |  Medium
https://leetcode.com/problems/lru-cache/

Design a Least Recently Used (LRU) cache with capacity `capacity`, supporting:
    get(key)         -- return the value if key exists, else -1.
                         Using a key counts as "recently used".
    put(key, value)  -- insert/update the value. If this exceeds capacity,
                         evict the least recently used key first.

Both operations must run in O(1) average time.

Example:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)       -> 1        (1 is now most recent)
    cache.put(3, 3)                (evicts 2, the LRU key)
    cache.get(2)       -> -1
    cache.put(4, 4)                (evicts 1)
    cache.get(1)       -> -1
    cache.get(3)       -> 3
    cache.get(4)       -> 4

Constraints:
    1 <= capacity <= 3000
    0 <= key, value <= 10^4
    Up to 2 * 10^5 calls total.

Hint:
    A dict alone gives O(1) lookup but no ordering. A doubly linked list gives
    O(1) reordering but no lookup. Combine them: dict maps key -> node, and the
    list keeps nodes in recency order (move-to-front/back on touch, evict from
    the opposite end). Sentinel head/tail nodes remove edge cases when
    inserting or removing at the boundaries.

Target complexity: O(1) time per operation, O(capacity) space
"""
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        pass
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

        pass

    def _remove(self , node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def _addtofront(self,node):
        first = self.head.next
        self.head.next = node
        node.prev = self.head

        node.next = first
        first.prev = node



    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._addtofront(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._addtofront(node)

        else:
            node = Node(key,value)
            self._addtofront(node)
            self.map[key] = node
            if len(self.map)>self.capacity:
                lru = self.tail.prev
                self.tail.prev = lru.prev
                lru.prev.next =self.tail

                del self.map[lru.key]
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
