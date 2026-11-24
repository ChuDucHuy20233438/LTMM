
def hex_to_bytes(hex_string):
    """Chuyen chuoi hex thanh bytes."""
    hex_string = hex_string.replace("0x", "")
    hex_string = hex_string.replace(" ", "")

    if len(hex_string) % 2 != 0:
        raise ValueError("So ky tu hex phai chan")

    return bytes.fromhex(hex_string)


def bytes_to_hex(data):
    """Chuyen bytes thanh chuoi hex."""
    return data.hex().upper()


def bytes_to_state(data):
    """Nap 16 byte vao ma tran State 4x4 theo cot."""
    if len(data) != 16:
        raise ValueError("AES State phai co dung 16 byte")

    state = [[0] * 4 for _ in range(4)]

    for r in range(4):
        for c in range(4):
            state[r][c] = data[4 * c + r]

    return state


def state_to_bytes(state):
    """Chuyen ma tran State thanh 16 byte theo cot."""
    result = []

    for c in range(4):
        for r in range(4):
            result.append(state[r][c])

    return bytes(result)


def print_state(title, state):
    """In ma tran State."""
    print("\n" + title)

    for row in state:
        print(" ".join(f"{value:02X}" for value in row))


def xor_bytes(a, b):
    """XOR hai day byte co cung do dai."""
    if len(a) != len(b):
        raise ValueError("Hai day byte phai co cung do dai")

    return bytes(x ^ y for x, y in zip(a, b))
