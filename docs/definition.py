def ternary_xor(𝑎, 𝑏, 𝑐):
    return 𝑎 ^ 𝑏 ^ 𝑐

def is_cyclic_under_ternary_xor(𝛹):
    for 𝑎 in 𝛹:
        for 𝑏 in 𝛹:
            for 𝑐 in 𝛹:
                𝑥 = ternary_xor(𝑎, 𝑏, 𝑐)
                if 𝑥 not in 𝛹:
                    return False
    return True