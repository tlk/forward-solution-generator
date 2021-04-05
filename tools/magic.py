#!/usr/bin/env python3
import itertools, sys
from game import ngame, nreverse

def usage():
    message = """
    Generate a game solution to stdout.
    Example usage: magic.py 'Hello there!'
    """
    print(message, file=sys.stderr)
    sys.exit(1)

def build_mixer_table(target):
    m = bytes.fromhex("576861742068617665204920676f743f")
    y = bytes.fromhex("2a6fc638d23abc155308c1e3de83e226")

    pocket = [i ^ n for i, n in zip(m, y)]

    table = {}

    for lower_index in pocket:
        l_value = ngame.sbox[lower_index]

        for upper_index in pocket:
            u_value = ngame.sbox[upper_index+256]

            letter = chr(l_value ^ u_value)

            if letter in target:
                table[letter] = (lower_index, upper_index)

    return table

def reverse(target):
    mixer_table = build_mixer_table(target)
    s_table = nreverse.build_substitution_table()

    c = []
    for letter in target:
        a, b = mixer_table[letter]
        c.append(a)
        c.append(b)

    for _ in range(256):
        s = nreverse.reverse_permutation(c)
        c = [s_table.get(letter)[0] for letter in s]

    return c

if __name__ == "__main__":

    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        usage()

    """
    Ensure target length is 16 characters, possibly space-padded.
    """
    target = f"{(target[:16]):<16}"

    """
    Generate a solution in constant time.
    """
    solution = reverse(target)
    print("".join(f"{byte:02x}" for byte in solution))
