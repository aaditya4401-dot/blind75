"""
Encode and Decode Strings  |  LeetCode 271  |  Medium
https://leetcode.com/problems/encode-and-decode-strings/

[LeetCode Premium] Design an algorithm to encode a list of strings into a
single string, and decode that string back into the original list.

    encode(["lint", "code", "love", "you"]) -> some string
    decode(that string) -> ["lint", "code", "love", "you"]

Example 1:
    Input:  ["hello", "world"]
    Output: ["hello", "world"]  (after a round trip)

Example 2:
    Input:  [""]
    Output: [""]

Constraints:
    The strings may contain ANY characters, including your delimiter, newlines
    and the empty string.

Hint:
    Any plain delimiter is breakable, because the data can contain it. Use
    length prefixing instead: write "<len>#<string>" for each entry. To decode,
    read digits up to the '#', then take exactly that many characters and
    continue from there.

    Test it against ["#", "3#abc", ""] -- inputs that break delimiter-only
    schemes.

Target complexity: O(total length) for both directions
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        pass

    def decode(self, s: str) -> List[str]:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_encode_and_decode_strings.py"))]))
