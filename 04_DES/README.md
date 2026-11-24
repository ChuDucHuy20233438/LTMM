
# DES Encryption Algorithm

## 1. Introduction

This project implements the Data Encryption Standard (DES) algorithm using Python. It supports 64-bit block encryption and decryption with a 64-bit input key.

## 2. Algorithm

DES is a symmetric block cipher consisting of:
- Initial Permutation (IP).
- 16 Feistel rounds.
- Key schedule generating 16 round keys (48 bits each).
- Final Permutation (IP inverse).

## 3. Project Structure

```text
04_DES/
├── main.py
├── des.py
├── key_schedule.py
├── tables.py
├── utils.py
├── test_vectors.py
└── README.md
```

## 4. Usage

Run the program:

```bash
python main.py
```

Run the test suite:

```bash
python test_vectors.py
```

## 5. Test Results

Standard test vector:

- Plaintext: `0123456789ABCDEF`
- Key: `133457799BBCDFF1`
- Ciphertext: `85E813540F0AB405`

Project test vector:

- Plaintext: `0000000000000011`
- Key: `0000000000000000`
- Ciphertext: `799A09FB40DF6019`

All encryption, decryption, and key schedule tests passed.

## 6. Note

DES is implemented for educational purposes. It is considered insecure for modern applications due to its short effective key length.
