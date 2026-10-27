def decrypt(text, shift):
    result = ''
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base - shift) % 26 + base)
        else:
            result += ch
    return result

cipher = input("Enter ciphertext: ")

# Rough English letter-frequency scoring
frequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def score(text):
    letters = [c.upper() for c in text if c.isalpha()]
    return sum(frequency.index(c) for c in letters) if letters else 0

candidates = sorted(
    [(score(decrypt(cipher, s)), s, decrypt(cipher, s))
     for s in range(26)]
)

print("Top 10 possible plaintexts:")
for _, shift, plain in candidates[:10]:
    print(f"Shift {shift:2}: {plain}")