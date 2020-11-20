import pytest
from lib.key_generator import *

def test_it_can_take_date_and_generate_offsets():
    key_gen = KeyGenerator()
    assert key_gen.make_offsets('040895') == [1, 0, 2, 5]
