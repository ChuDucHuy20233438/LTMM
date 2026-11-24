
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
