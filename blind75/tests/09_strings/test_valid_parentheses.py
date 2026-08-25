"""Tests for Valid Parentheses. Run: pytest 09_strings/test_valid_parentheses.py"""
import pytest

from valid_parentheses import Solution

@pytest.mark.parametrize("s, expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("(", False),
    (")", False),
    ("((", False),
    ("]", False),
    ("({[]})", True),
])
def test_is_valid(s, expected):
    assert Solution().isValid(s) is expected

