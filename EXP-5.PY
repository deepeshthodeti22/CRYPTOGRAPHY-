
from math import gcd


def affine_encrypt(text, a, b):
    result = ""

    for ch in text:
        if ch.isupper():
            x = ord(ch) - ord('A')
            result += chr((a * x + b) % 26 + ord('A'))
        elif ch.islower():
            x = ord(ch) - ord('a')
            result += chr((a * x + b) % 26 + ord('a'))
        else:
            result += ch

    return result


def affine_decrypt(text, a, b):
    result = ""
    inverse = pow(a, -1, 26)

    for ch in text:
        if ch.isupper():
            y = ord(ch) - ord('A')
            result += chr((inverse * (y - b)) % 26 + ord('A'))
        elif ch.islower():
            y = ord(ch) - ord('a')
            result += chr((inverse * (y - b)) % 26 + ord('a'))
        else:
            result += ch

    return result


text = input("Enter plaintext: ")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

if gcd(a, 26) != 1:
    print("Invalid a! Choose a value coprime with 26.")
else:
    encrypted = affine_encrypt(text, a, b)
    print("Encrypted text:", encrypted)
    print("Decrypted text:", affine_decrypt(encrypted, a, b))
