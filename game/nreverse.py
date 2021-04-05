import itertools

from game import ngame
from game import nforward_unrolled

def reverse(target, rounds=256):
    mixer_table = build_mixer_table(target)
    reverse_substitution_table = build_substitution_table()

    for candidate in mixer_candidates(mixer_table, target):
        yield from reverse_sp_network(reverse_substitution_table, candidate, rounds)

def build_mixer_table(target):
    table = { letter: [] for letter in target }

    for lower_index in range(256):
        l_value = ngame.sbox[lower_index]

        for upper_index in range(256):
            u_value = ngame.sbox[upper_index+256]

            letter = chr(l_value ^ u_value)

            if letter in target:
                table[letter].append((lower_index, upper_index))

    return table

def build_substitution_table():
    table = { value: [] for value in ngame.sbox[:256] }

    for index in range(256):
        value = ngame.sbox[index]
        table[value].append(index)

    return table

def mixer_candidates(mixer_table, target):
    assert len(target) % 2 == 0, "target must have an even length"
    letter_pos_candidates = (mixer_table[letter] for letter in target)
    for mixer_pairs in itertools.product(*letter_pos_candidates):
        yield list(itertools.chain(*mixer_pairs))

def reverse_sp_network(s_table, candidate, level=256):

    next_level = level - 1

    if next_level == 0:
        yield from reverse_single_round(s_table, candidate)

    else:
        for next_level_candidate in reverse_single_round(s_table, candidate):
            yield from reverse_sp_network(s_table, next_level_candidate, next_level)

def reverse_single_round(s_table, inp):
    target = reverse_permutation(inp)
    return substitution_candidates(s_table, target)

def reverse_permutation(inp):
    return nforward_unrolled.permute(inp)

def substitution_candidates(s_table, target):

    is_deadend = (target[ 0] not in s_table or target[ 1] not in s_table or
                  target[ 2] not in s_table or target[ 3] not in s_table or
                  target[ 4] not in s_table or target[ 5] not in s_table or
                  target[ 6] not in s_table or target[ 7] not in s_table or
                  target[ 8] not in s_table or target[ 9] not in s_table or
                  target[10] not in s_table or target[11] not in s_table or
                  target[12] not in s_table or target[13] not in s_table or
                  target[14] not in s_table or target[15] not in s_table or
                  target[16] not in s_table or target[17] not in s_table or
                  target[18] not in s_table or target[19] not in s_table or
                  target[20] not in s_table or target[21] not in s_table or
                  target[22] not in s_table or target[23] not in s_table or
                  target[24] not in s_table or target[25] not in s_table or
                  target[26] not in s_table or target[27] not in s_table or
                  target[28] not in s_table or target[29] not in s_table or
                  target[30] not in s_table or target[31] not in s_table)

    if is_deadend:
        return

    letter_options = (s_table.get(letter) for letter in target)
    yield from itertools.product(*letter_options)
