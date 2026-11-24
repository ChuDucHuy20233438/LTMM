
from aes import SBOX


def rot_word(word):
    """Dich xoay trai mot tu 4 byte."""
    return word[1:] + word[:1]


def sub_word(word):
    """Thay the tung byte bang gia tri trong S-box."""
    return [SBOX[value] for value in word]


def xor_words(word_a, word_b):
    """Thuc hien XOR hai tu 4 byte."""
    if len(word_a) != 4 or len(word_b) != 4:
        raise ValueError("Moi tu AES phai co dung 4 byte")

    return [
        word_a[i] ^ word_b[i]
        for i in range(4)
    ]


RCON = [
    0x00,
    0x01, 0x02, 0x04, 0x08, 0x10,
    0x20, 0x40, 0x80, 0x1B, 0x36
]

def key_expansion(key):
    """Mo rong khoa AES-128 thanh 11 khoa vong."""

    if len(key) != 16:
        raise ValueError("Khoa AES-128 phai co dung 16 byte")

    # Chia khoa ban dau thanh 4 tu, moi tu 4 byte
    words = []

    for i in range(4):
        words.append(list(key[4 * i:4 * i + 4]))

    # Tao them 40 tu de co tong cong 44 tu
    for i in range(4, 44):
        temp = words[i - 1].copy()

        if i % 4 == 0:
            temp = rot_word(temp)
            temp = sub_word(temp)
            temp[0] ^= RCON[i // 4]

        new_word = xor_words(words[i - 4], temp)
        words.append(new_word)

    # Gom 44 tu thanh 11 khoa vong
    round_keys = []

    for round_number in range(11):
        round_key = []

        for word_number in range(4):
            round_key.extend(
                words[round_number * 4 + word_number]
            )

        round_keys.append(bytes(round_key))

    return round_keys


def print_round_keys(round_keys):
    """In 11 khoa vong duoi dang hexadecimal."""

    for i, round_key in enumerate(round_keys):
        print(f"Khoa vong {i:02d}: {round_key.hex().upper()}")
