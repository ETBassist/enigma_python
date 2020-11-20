import pytest
from lib.rotator import *

def test_it_can_right_rotate_an_array():
    rotator = Rotator()
    original = [1, 2, 3, 4, 5, 6]
    expected = [3, 4, 5, 6, 1, 2]
    assert rotator.right_rotate(original, 2) == expected
    
def test_it_can_left_rotate_an_array():
    rotator = Rotator()
    original = [1, 2, 3, 4, 5, 6]
    expected = [4, 5, 6, 1, 2, 3]
    assert rotator.left_rotate(original, 2) == expected
