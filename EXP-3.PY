
def create_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    letters = ""

    for ch in (key + alphabet):
        ch = ch.upper()
        if ch == 'J':
            ch = 'I'
        if ch in alphabet and ch not in letters:
            letters += ch

    return [list(letters[i:i+5]) for i in range(0, 25, 5)]


def prepare_text(text):
    text = ''.join(
        ch for ch in text.upper() if ch.isalpha()
    ).replace('J', 'I')

    pairs = []
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 >= len(text):
            b = 'X'
            i += 1
        elif text[i + 1] == a:
            b = 'X'
            i += 1
        else:
            b = text[i + 1]
            i += 2

        pairs.append((a, b))

    return pairs


def playfair_encrypt(text, key):
    matrix = create_matrix(key)
    positions = {
        matrix[r][c]: (r, c)
        for r in range(5) for c in range(5)
    }

    result = ""

    for a, b in prepare_text(text):
        r1, c1 = positions[a]
        r2, c2 = positions[b]

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Enter keyword: ")
text = input("Enter plaintext: ")

print("Encrypted text:", playfair_encrypt(text, key))
