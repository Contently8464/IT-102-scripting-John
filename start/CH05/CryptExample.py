#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By John Gurney
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
key = os.urandom(32)
iv = os.urandom(16)
plaintext = b'Confidential message'
padder = padding.PKCS7(128).padder()
padded_data = padder.update(plaintext) + padder.finalize()
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()
print("Ciphertext:", ciphertext.hex())

decryptor = cipher.decryptor()
decrypted_packets = decryptor.update(ciphertext) + decryptor.finalize()
unpadder = padding.PKCS7(128).unpadder()
decrypted_data = unpadder.update(decrypted_packets) + unpadder.finalize()
print("Decrypted:", decrypted_data.decode())