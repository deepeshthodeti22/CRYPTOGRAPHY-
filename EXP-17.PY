from Crypto.Cipher import DES

key = bytes.fromhex(input("Enter 16-digit hex key: "))
ciphertext = bytes.fromhex(input("Enter ciphertext in hex: "))

if len(key) != 8 or len(ciphertext) % 8 != 0:
    print("Invalid DES key or ciphertext length!")
else:
    des = DES.new(key, DES.MODE_ECB)
    plaintext = des.decrypt(ciphertext)
    print("Decrypted bytes:", plaintext)
    print("Plaintext (hex):", plaintext.hex())