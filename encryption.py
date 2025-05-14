from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes
import hashlib

#First, take string Password and encrypt it using AES encryption.
def password_encrypt(password):
    data = str(password).encode()

    aes_key = get_random_bytes(16)
    hmac_key = get_random_bytes(16)

    cipher = AES.new(aes_key, AES.MODE_CTR)
    ciphertext = cipher.encrypt(data)

    hmac = HMAC.new(hmac_key,digestmod=SHA256)
    tag = hmac.update(cipher.nonce + ciphertext).digest()

#take the encrypted password, and hash it using SHA256 hashing algorithm.
def hash_encrypted_bytes():
    pass

#store that hash in a CSV file with the name "password_hash.csv"

#create function to check the encrypted password against hash, and if it matches
#then unencrypt the pasw sword and return it.