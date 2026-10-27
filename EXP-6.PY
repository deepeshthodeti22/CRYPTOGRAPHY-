from math import gcd

def decrypt(text, a, b):
    inv = pow(a, -1, 26)
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((inv * (ord(ch) - ord('A') - b)) % 26 + ord('A'))
        elif ch.islower():
            result += chr((inv * (ord(ch) - ord('a') - b)) % 26 + ord('a'))
        else:
            result += ch

    return result


cipher = input("Enter ciphertext: ")

print("\nPossible plaintexts:")

for a in range(1, 26):
    if gcd(a, 26) == 1:
        for b in range(26):
            print(f"a={a:2}, b={b:2}: {decrypt(cipher, a, b)}")