# AES-128 Encryption

## 1. Giới thiệu
Dự án xây dựng thuật toán mã hóa AES-128 bằng Python. Thuật toán sử dụng khối dữ liệu 128 bit, khóa 128 bit và thực hiện 10 vòng mã hóa.

## 2. Cấu trúc dự án

```text
03_ASE_128/
├── utils.py
├── aes.py
├── key_expansion.py
├── main.py
├── test_vectors.py
├── README.md
└── results/
    └── aes_output.txt
```

## 3. Chức năng các file

- `utils.py`: Các hàm xử lý và chuyển đổi dữ liệu.
- `aes.py`: Các phép biến đổi SubBytes, ShiftRows, MixColumns, AddRoundKey và xử lý GF(2⁸).
- `key_expansion.py`: Mở rộng khóa AES-128.
- `main.py`: Thực hiện mã hóa AES-128.
- `test_vectors.py`: Kiểm thử thuật toán.
- `results/aes_output.txt`: Lưu kết quả mã hóa.

## 4. Cách chạy chương trình

Chạy mã hóa:

```bash
python main.py
```

Chạy kiểm thử:

```bash
python -m unittest test_vectors -v
```

## 5. Vector kiểm thử

- **Key:** `000102030405060708090A0B0C0D0E0F`
- **Plaintext:** `00112233445566778899AABBCCDDEEFF`
- **Ciphertext:** `69C4E0D86A7B0430D8CDB78070B4C55A`

## 6. Kết luận

Dự án đã triển khai các thành phần chính của AES-128, thực hiện mã hóa dữ liệu và kiểm thử kết quả bằng vector chuẩn.