import string
from rotator import *

class Enigma:
    def __init__(self):
        rotor = Rotator()

    def encrypt(self, phrase, key, date):
        alphabet = list(string.ascii_lowercase)
