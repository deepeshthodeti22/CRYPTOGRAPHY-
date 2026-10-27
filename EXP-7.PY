def decrypt(cipher, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for ch in cipher:
        if ch.isupper():
            result += key[ord(ch) - ord('A')]
        elif ch.islower():
            result += key[ord(ch) - ord('a')].lower()
        else:
            result += ch

    return result


key = input("Enter decryption key (26 letters): ").upper()

if len(key) != 26 or not key.isalpha() or len(set(key)) != 26:
    print("Invalid key!")
else:
    cipher = input("Enter ciphertext: ")
    print("Plaintext:", decrypt(cipher, key))