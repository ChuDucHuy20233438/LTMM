from des import des_encrypt, des_decrypt
from key_schedule import generate_round_keys


# Vector DES tieu chuan
STANDARD_PLAINTEXT = 0x0123456789ABCDEF
STANDARD_KEY = 0x133457799BBCDFF1
STANDARD_CIPHERTEXT = 0x85E813540F0AB405


# Vector kiem thu cua du an
PROJECT_PLAINTEXT = 0x0000000000000011
PROJECT_KEY = 0x0000000000000000
def test_key_schedule():
    """Kiem tra qua trinh sinh 16 khoa vong."""

    round_keys = generate_round_keys(STANDARD_KEY)

    assert len(round_keys) == 16
    assert all(0 <= key < (1 << 48) for key in round_keys)

    assert round_keys[0] == 0x1B02EFFC7072

    print("[PASS] Key schedule")