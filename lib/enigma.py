import string
from rotator import Rotator
from key_generator import KeyGenerator

class Enigma:
    def __init__(self):
        self.rotor = Rotator()
        self.key_gen = KeyGenerator()

    def encrypt(self, phrase, key, date):
        cipher = self.key_gen.make_cipher(key, date)
        result = []
        for char_index, letter in enumerate(phrase):
            alphabet = list(string.ascii_lowercase)
            alphabet.append(' ')
            if letter in alphabet:
                index = alphabet.index(letter)
                rotated_alpha = self.rotor.left_rotate(alphabet, cipher[char_index % 4])
                result.append(rotated_alpha[index])
            else:
                result.append(letter)
        return ''.join(result)

    def decrypt(self, encrypted_phrase, key, date):
        cipher = self.key_gen.make_cipher(key, date)
        result = []
        for char_index, letter in enumerate(encrypted_phrase):
            alphabet = list(string.ascii_lowercase)
            alphabet.append(' ')
            if letter in alphabet:
                index = alphabet.index(letter)
                rotated_alpha = self.rotor.right_rotate(alphabet, cipher[char_index % 4])
                result.append(rotated_alpha[index])
            else:
                result.append(letter)
        return ''.join(result)

