from lib import ngame

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

unroll_permutation_box()
