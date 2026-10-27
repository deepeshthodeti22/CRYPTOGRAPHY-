def encrypt(text, key):
    text = ''.join(c for c in text.upper() if c.isalpha())

    if len(text) != len(key):
        raise ValueError("Key length must equal the number of letters")

    cipher = ''
    for ch, k in zip(text, key):
        p = ord(ch) - ord('A')
        cipher += chr((p + k) % 26 + ord('A'))
    return cipher

def decrypt(cipher, key):
    result = ''
    for ch, k in zip(cipher, key):
        c = ord(ch) - ord('A')
        result += chr((c - k) % 26 + ord('A'))
    return result

plaintext = input("Enter plaintext: ")
key = list(map(int, input("Enter key stream: ").split()))

cipher = encrypt(plaintext, key)
print("Ciphertext:", cipher)
print("Decrypted text:", decrypt(cipher, key))