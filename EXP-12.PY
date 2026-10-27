from math import gcd

def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

def hill_encrypt(text, key):
    text = ''.join(c for c in text.upper() if c.isalpha())
    if len(text) % 2:
        text += 'X'

    result = ''
    for i in range(0, len(text), 2):
        x = ord(text[i]) - 65
        y = ord(text[i + 1]) - 65

        c1 = (key[0][0] * x + key[0][1] * y) % 26
        c2 = (key[1][0] * x + key[1][1] * y) % 26

        result += chr(c1 + 65) + chr(c2 + 65)
    return result

def hill_decrypt(cipher, key):
    det = (key[0][0] * key[1][1]
           - key[0][1] * key[1][0]) % 26
    inv = mod_inverse(det, 26)

    if inv is None:
        raise ValueError("Key matrix is not invertible modulo 26")

    inverse_key = [
        [(inv * key[1][1]) % 26, (-inv * key[0][1]) % 26],
        [(-inv * key[1][0]) % 26, (inv * key[0][0]) % 26]
    ]

    result = ''
    for i in range(0, len(cipher), 2):
        x = ord(cipher[i]) - 65
        y = ord(cipher[i + 1]) - 65

        p1 = (inverse_key[0][0] * x +
              inverse_key[0][1] * y) % 26
        p2 = (inverse_key[1][0] * x +
              inverse_key[1][1] * y) % 26

        result += chr(p1 + 65) + chr(p2 + 65)
    return result

key = [[9, 4], [5, 7]]
message = input("Enter plaintext: ")

cipher = hill_encrypt(message, key)
print("Encrypted text:", cipher)
print("Decrypted text:", hill_decrypt(cipher, key))