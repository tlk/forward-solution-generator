def unroll_substitution_box():
    for i in range(32):
        if i % 8 == 0:
            print()
        print(f"sbox[c[{i:2}]], ", end="")
    print()

unroll_substitution_box()
