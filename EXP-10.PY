matrix = [
    list("MFHIK"),
    list("UNOPQ"),
    list("ZVWXY"),
    list("ELARG"),
    list("DSTBC")
]


def find_position(ch):
    if ch == 'J':
        ch = 'I'

    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c


def prepare_text(text):
    text = ''.join(ch for ch in text.upper() if ch.isalpha())
    text = text.replace('J', 'I')
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 >= len(text):
            b = 'X'
            i += 1
        elif text[i] == text[i + 1]:
            b = 'X'
            i += 1
        else:
            b = text[i + 1]
            i += 2

        pairs.append((a, b))

    return pairs


def encrypt(text):
    result = ""

    for a, b in prepare_text(text):
        r1, c1 = find_position(a)
        r2, c2 = find_position(b)

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


message = "Must see you over Cadogan West. Coming at once."
print("Encrypted text:", encrypt(message))