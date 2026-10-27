from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

key = DES3.adjust_key_parity(bytes.fromhex(
    "0123456789ABCDEFFEDCBA98765432100011223344556677"
))
iv = bytes.fromhex("1234567890ABCDEF")

message = b"BLOCK001BLOCK002BLOCK003BLOCK004"

def encrypt_ecb(data):
    return DES3.new(key, DES3.MODE_ECB).encrypt(pad(data, 8))

def encrypt_cbc(data):
    return DES3.new(key, DES3.MODE_CBC, iv).encrypt(pad(data, 8))

def decrypt_ecb(data):
    return DES3.new(key, DES3.MODE_ECB).decrypt(data)

def decrypt_cbc(data):
    return DES3.new(key, DES3.MODE_CBC, iv).decrypt(data)

def flip_bit(data, block_index):
    damaged = bytearray(data)
    damaged[block_index * 8] ^= 1
    return bytes(damaged)

ecb = encrypt_ecb(message)
cbc = encrypt_cbc(message)

print("Original plaintext:", message)

ecb_bad = flip_bit(ecb, 1)
cbc_bad = flip_bit(cbc, 1)

print("\nECB corrupted block:")
print(decrypt_ecb(ecb_bad))

print("\nCBC corrupted block:")
print(decrypt_cbc(cbc_bad))