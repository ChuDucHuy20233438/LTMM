
import unittest

from aes import (
    gf_mul,
    SBOX
)

from key_expansion import key_expansion

from utils import (
    bytes_to_state,
    state_to_bytes
)


class TestAES128(unittest.TestCase):

    def test_gf_multiplication(self):
        """Kiem tra phep nhan trong GF(2^8)."""
        self.assertEqual(gf_mul(0x57, 0x13), 0xFE)

    def test_sbox_values(self):
        """Kiem tra mot so gia tri trong bang S-box."""
        self.assertEqual(SBOX[0x00], 0x63)
        self.assertEqual(SBOX[0x01], 0x7C)
        self.assertEqual(SBOX[0x11], 0x82)
        self.assertEqual(SBOX[0x53], 0xED)

    def test_state_conversion(self):
        """Kiem tra chuyen doi giua bytes va State."""
        data = bytes.fromhex(
            "00112233445566778899AABBCCDDEEFF"
        )

        state = bytes_to_state(data)

        self.assertEqual(
            state,
            [
                [0x00, 0x44, 0x88, 0xCC],
                [0x11, 0x55, 0x99, 0xDD],
                [0x22, 0x66, 0xAA, 0xEE],
                [0x33, 0x77, 0xBB, 0xFF]
            ]
        )

        self.assertEqual(state_to_bytes(state), data)

    def test_key_expansion(self):
        """Kiem tra mo rong khoa AES-128."""
        key = bytes.fromhex(
            "000102030405060708090A0B0C0D0E0F"
        )

        round_keys = key_expansion(key)

        self.assertEqual(len(round_keys), 11)

        self.assertEqual(
            round_keys[0].hex().upper(),
            "000102030405060708090A0B0C0D0E0F"
        )

        self.assertEqual(
            round_keys[1].hex().upper(),
            "D6AA74FDD2AF72FADAA678F1D6AB76FE"
        )

    def test_shift_rows(self):
        """Kiem tra phep dich hang."""
        from aes import shift_rows

        state = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15]
        ]

        expected = [
            [0, 1, 2, 3],
            [5, 6, 7, 4],
            [10, 11, 8, 9],
            [15, 12, 13, 14]
        ]

        self.assertEqual(shift_rows(state), expected)

    def test_mix_columns(self):
        """Kiem tra phep tron cot."""
        from aes import mix_columns

        state = [
            [0xDB, 0, 0, 0],
            [0x13, 0, 0, 0],
            [0x53, 0, 0, 0],
            [0x45, 0, 0, 0]
        ]

        expected = [
            [0x8E, 0, 0, 0],
            [0x4D, 0, 0, 0],
            [0xA1, 0, 0, 0],
            [0xBC, 0, 0, 0]
        ]

        self.assertEqual(mix_columns(state), expected)

    def test_aes128_encryption(self):
        """Kiem tra ma hoa AES-128 bang vector chuan."""
        from main import encrypt_block_hex

        plaintext = "00112233445566778899AABBCCDDEEFF"
        key = "000102030405060708090A0B0C0D0E0F"

        expected = "69C4E0D86A7B0430D8CDB78070B4C55A"

        ciphertext = encrypt_block_hex(plaintext, key)

        self.assertEqual(ciphertext, expected)


if __name__ == "__main__":
    unittest.main()
