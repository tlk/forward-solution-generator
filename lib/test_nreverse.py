import unittest
import itertools
from lib import nforward
from lib import nreverse

class TestNReverse(unittest.TestCase):
    def test_substitution_table(self):
        s_table = nreverse.build_substitution_table()
        self.assertEqual(len(s_table), 240)
        self.assertEqual(len(s_table[0x00]), 1)
        self.assertEqual(len(s_table[0x01]), 1)
        self.assertEqual(len(s_table[0xff]), 1)
        self.assertEqual(len(s_table[0x02]), 2)
        self.assertEqual(len(s_table[0xf7]), 2)

    def test_substitution_1(self):
        s_table = nreverse.build_substitution_table()
        out = [0x00,0xf7]
        candidates = nreverse.substitution_candidates(s_table, out)
        self.assertEqual([(106, 98), (106, 254)], list(candidates))

    def test_substitution_2(self):
        s_table = nreverse.build_substitution_table()
        inp = (ord(c) for c in "abcdefghijklmnopABCDEFGHIJKLMNOP")
        out = [0xad,0xf7,0x36,0x47,0xab,0xce,0x7f,0x56,0xca,0x00,0xe3,0xed,0xf1,0x38,0xd8,0x26,
               0x86,0xba,0x4d,0x39,0xa0,0x0e,0x8c,0x8a,0xd0,0xfe,0x59,0x96,0x49,0xe6,0xea,0x69];
        candidates = nreverse.substitution_candidates(s_table, out)
        self.assertTrue(tuple(inp) in list(candidates))

    def test_permutation(self):
        inp = [0x66,0xd5,0x4e,0x28,0x5f,0xff,0x6b,0x53,0xac,0x3b,0x34,0x14,0xb5,0x3c,0xb2,0xc6,
               0xa4,0x85,0x1e,0x0d,0x86,0xc7,0x4f,0xba,0x75,0x5e,0xcb,0xc3,0x6e,0x48,0x79,0x8f];

        tmp = nreverse.reverse_permute(inp)
        res = nreverse.reverse_permute(tmp)

        # ngame.pbox is invertible
        self.assertEqual(inp, res)

    def test_get_lower_twin_values(self):
        expected = [0x33,0xbc,0x78,0x02,0xe9,0x66,0xc6,0xa2,0x49,0x1c,0xf7,0xd8,0x2d,0x8d,0x93,0x57]
        result = nreverse.get_twin_values()
        self.assertEqual(result, expected)

    def test_get_upper_twin_values(self):
        expected = [0x59,0x3f,0x4e,0xd0,0x28,0xcb,0xba,0xdc,0x33,0xa1,0xad,0x42,0x55,0xb6,0x24,0xc7]
        result = nreverse.get_twin_values(256)
        self.assertEqual(result, expected)

    def test_xor_upper_and_lower_twin_values(self):
        lower_twin_values = nreverse.get_twin_values()
        upper_twin_values = nreverse.get_twin_values(256)

        expected = list()
        for i in range(256):
            expected.append(i)

        xor_values = list()
        for l, u in itertools.product(lower_twin_values, upper_twin_values):
            xor_values.append(l ^ u)

        # interesting property
        self.assertEqual(expected, sorted(xor_values))

    def test_build_limited_mixer_table(self):
        target = "ab"
        expected = {'a': [(77, 33), (77, 209), (209, 33), (209, 209)],
                    'b': [(111, 58), (111, 202), (237, 58), (237, 202)]}

        mixer_table = nreverse.build_mixer_table(target, limit_search_space=True)
        self.assertEqual(mixer_table, expected)

    def test_mixer_candidates_1(self):
        target = "ab"
        expected = [ord(l) for l in target]

        mixer_table = nreverse.build_mixer_table(target)
        candidates = nreverse.mixer_candidates(mixer_table, target)

        counter = 0
        for candidate in candidates:
            result = nforward.mix(candidate)
            self.assertEqual(result, expected)
            counter += 1

        self.assertEqual(counter, 256**2)

    def test_mixer_candidates_2(self):
        target = "abcdefghijklmnop"
        expected = [ord(l) for l in target]

        mixer_table = nreverse.build_mixer_table(target)
        candidates = nreverse.mixer_candidates(mixer_table, target)
        sample = [next(candidates), next(candidates), next(candidates)]

        for candidate in sample:
            result = nforward.mix(candidate)
            self.assertEqual(result, expected)

    def test_reverse_single_round(self):
        s_table = nreverse.build_substitution_table()
        inp = [0x66,0xd5,0x4e,0x28,0x5f,0xff,0x6b,0x53,0xac,0x3b,0x34,0x14,0xb5,0x3c,0xb2,0xc6,
               0xa4,0x85,0x1e,0x0d,0x86,0xc7,0x4f,0xba,0x75,0x5e,0xcb,0xc3,0x6e,0x48,0x79,0x8f];
        out = [0x8d,0xc2,0xe1,0x51,0xab,0x55,0x97,0xb4,0xf4,0x7a,0xc3,0x53,0xaa,0xd8,0xf3,0x94,
               0xb1,0x42,0x48,0x32,0xf8,0x2b,0xfb,0xa3,0xd9,0xec,0x45,0xb7,0xc1,0x48,0x1b,0x6]

        candidates = nreverse.reverse_single_round(s_table, out)
        self.assertTrue(tuple(inp) in list(candidates))
