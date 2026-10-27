def create_matrix(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = ""

    for ch in (keyword + alphabet).upper():
        if ch == 'J':
            ch = 'I'
        if ch in alphabet and ch not in key:
            key += ch

    return [list(key[i:i + 5]) for i in range(0, 25, 5)]


def find_position(matrix, ch):
    if ch == 'J':
        ch = 'I'

    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c


def playfair_decrypt(cipher, keyword):
    matrix = create_matrix(keyword)
    text = ''.join(ch for ch in cipher.upper() if ch.isalpha())
    result = ""

    if len(text) % 2 != 0:
        raise ValueError("Ciphertext must contain an even number of letters.")

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5]
            result += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1]
            result += matrix[(r2 - 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


keyword = input("Enter Playfair keyword: ")

cipher = """
KXJEY UREBE ZWEHE WRYTU HEYFS
KREHE GOYFI WTTTU OLKSY CAJPO
BOTEI ZONTX BYBNT GONEY CUZWR
GDSON SXBOU YWRHE BAAHY USEDQ
"""

print("Decrypted text:", playfair_decrypt(cipher, keyword))