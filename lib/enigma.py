import pdb
import string
from rotator import *
from key_generator import *

class Enigma:
    def __init__(self):
        self.rotor = Rotator()
        self.key_gen = KeyGenerator()

    def encrypt(self, phrase, key, date):
        cipher = self.key_gen.make_cipher(key, date)
        result = []
        for lindex, letter in enumerate(phrase):
            alphabet = list(string.ascii_lowercase)
            alphabet.append(' ')
            if letter in alphabet:
                index = alphabet.index(letter)
                rotated_alpha = self.rotor.rotate(alphabet, cipher[lindex % 4])
                result.append(rotated_alpha[index])
            else:
                result.append(letter)
        return ''.join(result)
