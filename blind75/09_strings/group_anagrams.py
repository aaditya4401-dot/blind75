"""
Group Anagrams  |  LeetCode 49  |  Medium
https://leetcode.com/problems/group-anagrams/

Group the anagrams in a list of strings together. The answer may be returned in
any order.

Example 1:
    Input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Example 2:
    Input:  strs = [""]
    Output: [[""]]

Constraints:
    1 <= len(strs) <= 10^4
    0 <= len(strs[i]) <= 100
    strs[i] is lowercase English letters.

Hint:
    Every anagram group needs one canonical key. Sorting each word is the easy
    key -- O(n * k log k). The faster key is a 26-length count tuple, which is
    O(n * k). Group into a defaultdict(list) and return its values.

Target complexity: O(n * k) time with a count key, O(n * k) space
"""

from typing import List
from collections import defaultdict,Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            key = frozenset(Counter(s).items())
            ans[key].append(s)
        
        return list(ans.values())
                
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
