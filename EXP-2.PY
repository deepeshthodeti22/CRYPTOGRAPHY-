
def substitute(text, alphabet, key):
    result = ""

    for ch in text:
        if ch.isupper():
            result += key[alphabet.index(ch)]
        elif ch.islower():
            result += key[alphabet.index(ch.upper())].lower()
        else:
            result += ch

    return result


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = input("Enter 26-letter substitution key: ").upper()

if len(key) != 26 or not key.isalpha() or len(set(key)) != 26:
    print("Invalid key! Enter 26 unique letters.")
else:
    text = input("Enter plaintext: ")
    encrypted = substitute(text, alphabet, key)
    print("Encrypted text:", encrypted)

    decrypted = substitute(encrypted, key, alphabet)
    print("Decrypted text:", decrypted)
