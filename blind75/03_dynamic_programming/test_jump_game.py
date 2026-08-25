"""Tests for Jump Game. Run: pytest 03_dynamic_programming/test_jump_game.py"""
import pytest

from jump_game import Solution

@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([0], True),
    ([1, 0], True),
    ([0, 1], False),
    ([2, 0, 0], True),
    ([1, 1, 1, 0], True),
    ([2, 5, 0, 0], True),
])
def test_can_jump(nums, expected):
    assert Solution().canJump(nums) is expected

