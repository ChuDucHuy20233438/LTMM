
from aes import (
    sub_bytes,
    shift_rows,
    mix_columns,
    add_round_key
)

from key_expansion import key_expansion
from utils import (
    bytes_to_state,
    state_to_bytes,
    print_state,
    hex_to_bytes,
    bytes_to_hex
)


def apply_round(state, round_key, final_round=False):
    """Thuc hien mot vong bien doi AES."""

    if len(round_key) != 16:
        raise ValueError("Khoa vong AES phai co 16 byte")

    # Buoc 1: Thay the byte
    state = sub_bytes(state)

    # Buoc 2: Dich cac hang
    state = shift_rows(state)

    # Buoc 3: Tron cac cot, bo qua o vong cuoi
    if not final_round:
        state = mix_columns(state)

    # Buoc 4: XOR voi khoa vong
    state = add_round_key(state, round_key)

    return state

def encrypt_block(plaintext, key):
    """Ma hoa mot khoi 128 bit bang AES-128."""

    if len(plaintext) != 16:
        raise ValueError("Ban ro phai co dung 16 byte")

    if len(key) != 16:
        raise ValueError("Khoa AES-128 phai co dung 16 byte")

    # Tao 11 khoa vong
    round_keys = key_expansion(key)

    # Chuyen ban ro thanh ma tran State
    state = bytes_to_state(plaintext)

    # Buoc khoi tao: AddRoundKey
    state = add_round_key(state, round_keys[0])

    # Thuc hien cac vong tu 1 den 9
    for round_number in range(1, 10):
        state = apply_round(
            state,
            round_keys[round_number]
        )

    # Vong thu 10: khong thuc hien MixColumns
    state = apply_round(
        state,
        round_keys[10],
        final_round=True
    )

    # Chuyen State thanh ban ma 16 byte
    return state_to_bytes(state)


def encrypt_block_hex(plaintext_hex, key_hex):
    """Ma hoa AES-128 voi dau vao va dau ra dang hexadecimal."""

    plaintext = hex_to_bytes(plaintext_hex)
    key = hex_to_bytes(key_hex)

    ciphertext = encrypt_block(plaintext, key)

    return bytes_to_hex(ciphertext)


if __name__ == "__main__":
    plaintext = "00112233445566778899AABBCCDDEEFF"
    key = "000102030405060708090A0B0C0D0E0F"

    ciphertext = encrypt_block_hex(plaintext, key)

    print("Ban ro: ", plaintext)
    print("Khoa:   ", key)
    print("Ban ma: ", ciphertext)
