import pytest
from lib.key_generator import *

def test_it_can_take_date_and_generate_offsets():
    key_gen = KeyGenerator()
    assert key_gen.make_offsets('040895') == [1, 0, 2, 5]

def test_it_can_take_four_digit_number_and_return_key():
    key_gen = KeyGenerator()
    assert key_gen.make_key('02715') == [2, 27, 71, 15]

def test_it_can_combine_keys_and_offsets_into_cipher():
    key_gen = KeyGenerator()
    offsets = [1, 0, 2, 5]
    key = [2, 27, 71, 15]
    assert key_gen.make_cipher(key, offsets) == [3, 27, 73, 20]
