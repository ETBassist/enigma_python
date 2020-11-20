import pytest
from lib.enigma import *

def test_it_can_encode_a_word():
    enigma = Enigma()
    assert enigma.encrypt('hello world', '02715', '040895') == 'keder ohulw'

def test_it_can_decode_a_message():
    enigma = Enigma()
    assert enigma.decrypt('keder ohulw', '02715', '040895') == 'hello world'
