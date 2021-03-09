from Crypto.Random import random
from computation import *


class Elgamal:
    def __init__(self):
        self.prime = None
        self.generator = None
        self.enc_private_key = None
        self.dec_private_key = None
        self.public_key = None

    def generate(self, bits):
        self.prime = generate_random_prime(bits)
        self.generator = find_primitive_root(self.prime)
        self.dec_private_key = random.randrange(2, self.prime-1)
        self.public_key = square_and_multiply(
            self.generator, self.dec_private_key) % self.prime

    def export_key(self):
        return self.public_key, self.prime, self.generator

    def encryption(self, beta, p, g, x):
        self.enc_private_key = random.randrange(2, p-1)

        temp_key = square_and_multiply(g, self.enc_private_key) % p

        mask_key = square_and_multiply(beta, self.enc_private_key) % p

        y = [ord(c) * mask_key % p for c in x]

        return y, temp_key

    def decryption(self, y, temp_key):
        # mask_key = square_and_multiply(temp_key, self.dec_private_key)

        inv_mask_key = square_and_multiply(
            temp_key, self.prime - self.dec_private_key - 1)

        x = "".join([chr(i * inv_mask_key % self.prime) for i in y])
        return x
