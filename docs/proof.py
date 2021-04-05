
def is_cyclic_under_three_value_xor(R):
    for x in R:
        for y in R:
            for z in R:
                if not (x ^ y ^ z) in R:
                    return False

    return True

is_cyclic_under_three_value_xor(bytes.fromhex("071928364c52637d8896a7b9c3ddecf2"))

