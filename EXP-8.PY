def generate_key(keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = ""

    for ch in keyword.upper() + alphabet:
        if ch.isalpha() and ch not in key:
            key += ch

    return key


keyword = "CIPHER"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = generate_key(keyword)

print("Plain alphabet :", alphabet)
print("Cipher alphabet:", key)

text = input("Enter plaintext: ")
result = ""

for ch in text:
    if ch.isupper():
        result += key[ord(ch) - ord('A')]
    elif ch.islower():
        result += key[ord(ch) - ord('a')].lower()
    else:
        result += ch

print("Encrypted text:", result)