#!/usr/bin/env python3
import itertools
from game import ngame

def get_magic_numbers(sbox=ngame.sbox):
    cycles = get_cycles(sbox)

    for number_of_combined_cycles in range(len(cycles)):

        for combined_cycles in itertools.combinations(cycles, r=number_of_combined_cycles):

            𝛹 = list(itertools.chain.from_iterable(combined_cycles))

            if is_cyclic_under_ternary_xor(𝛹) and has_full_coverage(𝛹):
                return sorted(𝛹)

def get_cycles(sbox=ngame.sbox):
    cycles = list()
    visited = set()

    for node in range(256):
        if node in visited:
            continue

        trail = list()

        while node not in visited:
            visited.add(node)
            trail.append(node)
            node = sbox[node]

        cycle_is_detected = node in trail

        if cycle_is_detected:
            start_index = trail.index(node)
            cycle = trail[start_index:]
            cycles.append(cycle)

    return cycles

def is_cyclic_under_ternary_xor(𝛹):
    𝑋 = (𝑎 ^ 𝑏 ^ 𝑐 for 𝑎, 𝑏, 𝑐 in itertools.combinations_with_replacement(𝛹, r=3))
    return all(𝑥 in 𝛹 for 𝑥 in 𝑋)

def has_full_coverage(𝛹, sbox=ngame.sbox):
    coverage = set(sbox[a] ^ sbox[b+256] for a,b in itertools.product(𝛹, 𝛹))
    return all(byte_value in coverage for byte_value in range(256))

if __name__ == "__main__":
    𝛹 = get_magic_numbers()
    print("".join(f"{𝑥:02x}" for 𝑥 in 𝛹))
