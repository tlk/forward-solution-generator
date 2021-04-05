#!/usr/bin/env python3
from game import ngame

def unroll_substitution_box():
    for i in range(32):
        if i % 8 == 0:
            print()
        print(f"sbox[c[{i:2}]], ", end="")
    print()

def unroll_permutation_box():
    for j in range(32):
        print_hat = False
        for k in range(32):
            if (ngame.pbox[j]>>k)&1:
                if print_hat:
                    print("^", end="")
                print_hat = True
                print(f"inp[{k:2}]", end="")
        print(",")

def unroll_mixer():
    for i in range(16):
        print(f"sbox[c[{i*2:2}]]^sbox[c[{i*2+1:2}]+256],")

if __name__ == "__main__":
    unroll_substitution_box()
    unroll_permutation_box()
    unroll_mixer()
