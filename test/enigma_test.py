import pytest
from lib.enigma import *

def test_it_can_encode_a_word():
    enigma = Enigma()
    assert enigma.encrypt('hello world', '02715', '040895') == 'keder ohulw'

