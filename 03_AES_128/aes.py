
def gf_mul(a, b):
    """Nhan hai byte trong truong GF(2^8)."""
    result = 0

    while b > 0:
        if b & 1:
            result ^= a

        a <<= 1

        if a & 0x100:
            a ^= 0x11B

        b >>= 1

    return result


def gf_pow(a, power):
    """Tinh luy thua cua mot byte trong GF(2^8)."""
    result = 1

    while power > 0:
        if power & 1:
            result = gf_mul(result, a)

        a = gf_mul(a, a)
        power >>= 1

    return result


def gf_inverse(a):
    """Tim nghich dao nhan cua mot byte trong GF(2^8)."""
    if a == 0:
        return 0

    return gf_pow(a, 254)

def rotate_left(value, shift):
    """Dich xoay trai mot byte."""
    return ((value << shift) | (value >> (8 - shift))) & 0xFF


def sbox_transform(value):
    """Thuc hien bien doi affine cua AES."""
    return (
        value
        ^ rotate_left(value, 1)
        ^ rotate_left(value, 2)
        ^ rotate_left(value, 3)
        ^ rotate_left(value, 4)
        ^ 0x63
    )


def generate_sbox():
    """Tao bang S-box AES tu phep nghich dao GF(2^8)."""
    sbox = []

    for value in range(256):
        inverse = gf_inverse(value)
        sbox.append(sbox_transform(inverse))

    return sbox


SBOX = generate_sbox()

def sub_bytes(state):
    """Thay the tung byte trong State bang S-box."""
    result = []

    for row in state:
        new_row = []

        for value in row:
            new_row.append(SBOX[value])

        result.append(new_row)

    return result


def shift_rows(state):
    """Dich vong trai cac hang cua State."""
    result = []

    for r in range(4):
        new_row = state[r][r:] + state[r][:r]
        result.append(new_row)

    return result

def mix_columns(state):
    """Bien doi cac cot cua State trong GF(2^8)."""
    result = [[0] * 4 for _ in range(4)]

    for c in range(4):
        a0 = state[0][c]
        a1 = state[1][c]
        a2 = state[2][c]
        a3 = state[3][c]

        result[0][c] = (
            gf_mul(a0, 0x02)
            ^ gf_mul(a1, 0x03)
            ^ a2
            ^ a3
        )

        result[1][c] = (
            a0
            ^ gf_mul(a1, 0x02)
            ^ gf_mul(a2, 0x03)
            ^ a3
        )

        result[2][c] = (
            a0
            ^ a1
            ^ gf_mul(a2, 0x02)
            ^ gf_mul(a3, 0x03)
        )

        result[3][c] = (
            gf_mul(a0, 0x03)
            ^ a1
            ^ a2
            ^ gf_mul(a3, 0x02)
        )

    return result

def add_round_key(state, round_key):
    """XOR State voi khoa vong 16 byte."""
    if len(round_key) != 16:
        raise ValueError("Khoa vong AES phai co 16 byte")

    result = [[0] * 4 for _ in range(4)]

    for r in range(4):
        for c in range(4):
            result[r][c] = state[r][c] ^ round_key[4 * c + r]

    return result
