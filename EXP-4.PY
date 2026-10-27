
def vigenere(text, key, decrypt=False):
    result = ""
    key = key.upper()
    j = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - ord('A')

            if decrypt:
                shift = -shift

            if ch.isupper():
                result += chr(
                    (ord(ch) - ord('A') + shift) % 26 + ord('A')
                )
            else:
                result += chr(
                    (ord(ch) - ord('a') + shift) % 26 + ord('a')
                )

            j += 1
        else:
            result += ch

    return result


text = input("Enter plaintext: ")
key = input("Enter keyword: ")

if not key.isalpha():
    print("Keyword must contain letters only.")
else:
    encrypted = vigenere(text, key)
    print("Encrypted text:", encrypted)
    print("Decrypted text:", vigenere(encrypted, key, True))
