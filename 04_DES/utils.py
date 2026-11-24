
def permute(value, table, input_width):
    """
    Hoan vi cac bit theo bang chi dinh.
    Vi tri bit trong bang duoc danh so tu 1, tinh tu trai sang phai.
    """
    result = 0

    for position in table:
        bit = (value >> (input_width - position)) & 1
        result = (result << 1) | bit

    return result


def left_rotate(value, shift, width):
    """
    Dich vong trai mot gia tri bit voi do dai width.
    """
    mask = (1 << width) - 1

    shift %= width
    value &= mask

    return ((value << shift) | (value >> (width - shift))) & mask


def xor_bits(a, b):
    """
    Thuc hien phep XOR hai gia tri.
    """
    return a ^ b


def split_block(value, half_width):
    """
    Chia mot khoi thanh hai nua trai va phai.
    """
    mask = (1 << half_width) - 1

    left = value >> half_width
    right = value & mask

    return left, right


def to_hex(value, width):
    """
    Chuyen so nguyen sang chuoi HEX voi do dai chi dinh.
    width la so bit.
    """
    digits = (width + 3) // 4
    return f"{value:0{digits}X}"
