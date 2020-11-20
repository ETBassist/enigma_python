import string
from rotator import Rotator
from key_generator import KeyGenerator

class Enigma:
    def __init__(self):
        self.rotor = Rotator()
        self.key_gen = KeyGenerator()

    def encrypt(self, phrase, key, date):
        phrase = phrase.lower()
        cipher = self.key_gen.make_cipher(key, date)
        encrypted = self.__rotate_phrase(phrase, cipher, 'left')
        return ''.join(encrypted)

    def decrypt(self, encrypted_phrase, key, date):
        encrypted_phrase = encrypted_phrase.lower()
        cipher = self.key_gen.make_cipher(key, date)
        decrypted = self.__rotate_phrase(encrypted_phrase, cipher, 'right')
        return ''.join(decrypted)

    def __rotate_phrase(self, phrase, cipher, direction):
        result = []
        for char_index, letter in enumerate(phrase):
            alphabet = self.__create_characters()
            if letter in alphabet:
                index = alphabet.index(letter)
                rotated_alpha = self.rotor.rotate(alphabet, cipher[char_index % 4], direction)
                result.append(rotated_alpha[index])
            else:
                result.append(letter)
        return result

    def __create_characters(self):
        alphabet = list(string.ascii_lowercase)
        alphabet.append(' ')
        return alphabet

