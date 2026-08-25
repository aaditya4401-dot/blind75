"""Tests for Valid Palindrome. Run: pytest 09_strings/test_valid_palindrome.py"""
import pytest

from valid_palindrome import Solution

@pytest.mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("", True),
    ("ab_a", True),
    ("0P", False),
    ("aa", True),
    (".,", True),
    ("Madam", True),
])
def test_is_palindrome(s, expected):
    assert Solution().isPalindrome(s) is expected

