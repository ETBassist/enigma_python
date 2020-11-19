import pytest
from lib.rotator import *

def test_it_can_rotate_an_array():
    rotator = Rotator()
    original = [1, 2, 3, 4, 5]
    expected = [3, 4, 5, 1, 2]
    assert rotator.rotate(original) == expected
