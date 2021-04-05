"""
Turn a string input into a byte array
"""
def parse_solution(data):
    data = data.strip()

    if data[:2] == "0x" and len(data) == 2*32 + 2:
        data = int(data[2:], 16)
    elif len(data) == 2*32:
        data = int(data, 16)
    elif len(data) == 32:
        data = int.from_bytes(data.encode(), byteorder="big")
    else:
        data = int(data)

    return data.to_bytes(length=32, byteorder="big")
