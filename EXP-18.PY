# Demonstration of DES key splitting and round shifts.
# The complete DES standard uses PC-1 and PC-2 permutation tables.

SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2,
                  1, 2, 2, 2, 2, 2, 2, 1]

def rotate_left(value, shift, bits=28):
    shift %= bits
    return ((value << shift) | (value >> (bits - shift))) & ((1 << bits) - 1)

def show_round_halves(c0, d0):
    c, d = c0, d0

    for round_no, shift in enumerate(SHIFT_SCHEDULE, start=1):
        c = rotate_left(c, shift)
        d = rotate_left(d, shift)

        print(f"Round {round_no:2}: C={c:07X}, D={d:07X}")

# Illustrative 28-bit halves after the PC-1 permutation.
c0 = 0x0F0F0F0
d0 = 0x0F0F0F0

show_round_halves(c0, d0)