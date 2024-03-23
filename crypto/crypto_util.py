import hashlib
from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Hash import HMAC
from Crypto.Util.Padding import pad, unpad

aes_key = get_random_bytes(16)

def aesEncrypt(data):
    cipher = AES.new(aes_key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    return ciphertext


def aesDecrypt(ciphertext):
    cipher = AES.new(aes_key, AES.MODE_ECB)
    data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    return data

def cbc_encrypt(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    return ciphertext

def cbc_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return data

ciphertext = aesEncrypt(bytes('赵俊', encoding='utf-8'))
print(ciphertext)
data = aesDecrypt(ciphertext)
print(data.decode('utf-8'))

