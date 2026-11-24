
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
