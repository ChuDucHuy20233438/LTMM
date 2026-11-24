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
    def test_encryption():
        """Kiem tra ket qua ma hoa DES."""

    ciphertext = des_encrypt(
        STANDARD_PLAINTEXT,
        STANDARD_KEY
    )

    assert ciphertext == STANDARD_CIPHERTEXT

    print("[PASS] DES encryption")
    print(f"       Ciphertext: {ciphertext:016X}")
    def test_decryption():
        """Kiem tra kha nang giai ma DES."""

    plaintext = des_decrypt(
        STANDARD_CIPHERTEXT,
        STANDARD_KEY
    )

    assert plaintext == STANDARD_PLAINTEXT

    print("[PASS] DES decryption")
    print(f"       Plaintext: {plaintext:016X}")
    def test_project_vector():
        """Kiem tra vector du lieu cua du an."""

    ciphertext = des_encrypt(
        PROJECT_PLAINTEXT,
        PROJECT_KEY
    )

    decrypted = des_decrypt(
        ciphertext,
        PROJECT_KEY
    )

    assert decrypted == PROJECT_PLAINTEXT

    print("[PASS] Project test vector")
    print(f"       Plaintext : {PROJECT_PLAINTEXT:016X}")
    print(f"       Key       : {PROJECT_KEY:016X}")
    print(f"       Ciphertext: {ciphertext:016X}")
    print(f"       Decrypted : {decrypted:016X}")
def run_all_tests():
    """Chay tat ca cac truong hop kiem thu."""

    print("========== DES TESTS ==========")

    test_key_schedule()
    test_encryption()
    test_decryption()
    test_project_vector()

    print("================================")
    print("All tests passed!")


if __name__ == "__main__":
    run_all_tests()