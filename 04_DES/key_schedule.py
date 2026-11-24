from tables import PC1, PC2, SHIFTS
from utils import permute, left_rotate, split_block
def generate_round_keys(key):
    """
    Tao 16 khoa vong DES, moi khoa co do dai 48 bit.

    Args:
        key: Khoa ban dau 64 bit.

    Returns:
        Danh sach 16 khoa vong, moi khoa 48 bit.
    """

    # Buoc 1: Hoan vi PC-1, tu 64 bit xuong 56 bit
    permuted_key = permute(key, PC1, 64)
    # Buoc 2: Chia khoa thanh hai nua 28 bit
    C, D = split_block(permuted_key, 28)
    # Buoc 3: Tao 16 khoa vong
    round_keys = []

    for shift in SHIFTS:
        # Dich vong trai hai nua khoa
        C = left_rotate(C, shift, 28)
        D = left_rotate(D, shift, 28)

        # Ghep C va D thanh khoa 56 bit
        combined_key = (C << 28) | D

        # Hoan vi PC-2, tao khoa vong 48 bit
        round_key = permute(combined_key, PC2, 56)

        round_keys.append(round_key)

    return round_keys