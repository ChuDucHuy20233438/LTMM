from tables import IP, IP_INV, E, P, S_BOXES
from key_schedule import generate_round_keys
from utils import permute, xor_bits, split_block
def feistel_function(right, round_key):
    """
    Ham Feistel: bien doi nua phai 32 bit thanh 32 bit.
    """

    # Buoc 1: Mo rong R tu 32 bit thanh 48 bit
    expanded = permute(right, E, 32)

    # Buoc 2: XOR voi khoa vong 48 bit
    mixed = xor_bits(expanded, round_key)

    # Buoc 3: Chia ket qua thanh 8 nhom, moi nhom 6 bit
    sbox_output = 0

    for i in range(8):
        shift = 42 - 6 * i
        block = (mixed >> shift) & 0x3F

        # Bit dau va bit cuoi xac dinh hang
        row = ((block & 0x20) >> 4) | (block & 0x01)

        # Bon bit o giua xac dinh cot
        col = (block >> 1) & 0x0F

        # Tra bang S-box tuong ung
        value = S_BOXES[i][row][col]

        sbox_output = (sbox_output << 4) | value

    # Buoc 4: Hoan vi P
    return permute(sbox_output, P, 32)