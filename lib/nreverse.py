import itertools
from lib import ngame
from lib import nforward_unrolled

def reverse(target, rounds=256, limit_search_space=False):
    mixer_table = build_mixer_table(target, limit_search_space)
    s_table = build_substitution_table()

    for candidate in mixer_candidates(mixer_table, target):
        yield from traverse(s_table, candidate, rounds)

def build_mixer_table(target, limit_search_space=False):
    table = { letter: [] for letter in target }

    if limit_search_space:
        lower_twin_values = get_twin_values()
        upper_twin_values = get_twin_values(256)

    for lower_index in range(256):
        l_value = ngame.sbox[lower_index]

        if limit_search_space and l_value not in lower_twin_values:
            continue

        for upper_index in range(256):
            u_value = ngame.sbox[upper_index+256]

            if limit_search_space and u_value not in upper_twin_values:
                continue

            xor_value = l_value ^ u_value
            letter = chr(xor_value)

            if letter in target:
                table[letter].append((lower_index, upper_index))

    return table

def get_twin_values(offset=0):
    s_table = build_substitution_table(offset)
    return [value for value, indexes in s_table.items() if len(indexes) == 2]

def build_substitution_table(offset=0):
    table = { value:[] for value in ngame.sbox[offset:offset+256] }

    for index in range(256):
        value = ngame.sbox[offset+index]
        table[value].append(index)

    return table

def mixer_candidates(mixer_table, target):
    assert len(target) % 2 == 0, "target must have an even length"
    letter_pos_candidates = (mixer_table[letter] for letter in target)
    for mixer_pairs in itertools.product(*letter_pos_candidates):
        yield list(itertools.chain(*mixer_pairs))

def traverse(s_table, candidate, rounds=256):
    if rounds == 0:
        solution = candidate
        yield solution
    else:
        for c in reverse_single_round(s_table, candidate):
            yield from traverse(s_table, c, rounds - 1)

def reverse_single_round(s_table, inp):
    target = reverse_permute(inp)
    return substitution_candidates(s_table, target)

def reverse_permute(inp):
    return nforward_unrolled.permute(inp)

def substitution_candidates(s_table, target):
    for letter in target:
        if not s_table.get(letter):
            # no dice
            return

    letter_options = (s_table.get(letter) for letter in target)
    yield from itertools.product(*letter_options)
