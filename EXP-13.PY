def matrix_inverse_2x2(m):
    det = (m[0][0] * m[1][1] -
           m[0][1] * m[1][0]) % 26

    inv = next((i for i in range(26)
                if (det * i) % 26 == 1), None)

    if inv is None:
        raise ValueError("Plaintext matrix is not invertible modulo 26")

    return [
        [(inv * m[1][1]) % 26, (-inv * m[0][1]) % 26],
        [(-inv * m[1][0]) % 26, (inv * m[0][0]) % 26]
    ]

def multiply(a, b):
    return [
        [(a[i][0] * b[0][j] + a[i][1] * b[1][j]) % 26
         for j in range(2)]
        for i in range(2)
    ]

# Columns represent two plaintext/ciphertext pairs.
P = [[7, 4],
     [4, 11]]

C = [[19, 0],
     [13, 19]]

try:
    P_inv = matrix_inverse_2x2(P)
    K = multiply(C, P_inv)
    print("Recovered key matrix:")
    for row in K:
        print(row)
except ValueError as e:
    print(e)