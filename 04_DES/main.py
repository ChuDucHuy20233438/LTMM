from des import des_encrypt, des_decrypt
def input_hex(message):
    """
    Nhap mot gia tri HEX 64 bit.
    """

    while True:
        try:
            value = input(message).strip()
            number = int(value, 16)

            if 0 <= number < (1 << 64):
                return number

            print("Gia tri phai nam trong pham vi 64 bit.")

        except ValueError:
            print("Du lieu khong hop le. Vui long nhap HEX.")
def display_menu():
    print("\n========== DES PROGRAM ==========")
    print("1. Ma hoa")
    print("2. Giai ma")
    print("0. Thoat")
    print("=================================")
def main():
    while True:
        display_menu()

        choice = input("Nhap lua chon: ").strip()

        if choice == "0":
            print("Ket thuc chuong trinh.")
            break

        elif choice == "1":
            plaintext = input_hex("Nhap ban ro (HEX): ")
            key = input_hex("Nhap khoa (HEX): ")

            ciphertext = des_encrypt(plaintext, key)

            print("Ban ma:", f"{ciphertext:016X}")

        elif choice == "2":
            ciphertext = input_hex("Nhap ban ma (HEX): ")
            key = input_hex("Nhap khoa (HEX): ")

            plaintext = des_decrypt(ciphertext, key)

            print("Ban ro:", f"{plaintext:016X}")

        else:
            print("Lua chon khong hop le!")
if __name__ == "__main__":
    main()