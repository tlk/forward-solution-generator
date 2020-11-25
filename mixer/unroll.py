def unroll_mixer():
    for i in range(16):
        print(f"sbox[c[{i*2:2}]]^sbox[c[{i*2+1:2}]+256],")

unroll_mixer()
