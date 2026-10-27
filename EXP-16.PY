from collections import Counter

ENGLISH_FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_attack(cipher):
    counts = Counter(c.upper() for c in cipher if c.isalpha())
    cipher_order = [
        ch for ch, _ in counts.most_common()
    ]

    remaining = [c for c in ENGLISH_FREQ if c not in cipher_order]
    cipher_order += remaining

    mapping = {
        ch: ENGLISH_FREQ[i]
        for i, ch in enumerate(cipher_order)
    }

    result = ''
    for ch in cipher:
        if ch.isalpha():
            plain = mapping[ch.upper()]
            result += plain if ch.isupper() else plain.lower()
        else:
            result += ch

    return result

cipher = input("Enter ciphertext: ")
print("Frequency-based candidate:")
print(frequency_attack(cipher))
print("\nNote: This is an approximate candidate, not guaranteed plaintext.")