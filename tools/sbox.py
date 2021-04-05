#!/usr/bin/env python3
from game import ngame

print('digraph {')
print('layout=circo')

for n in range(256):
    print(f'"{n}" -> "{ ngame.sbox[n] }";')

print('}')
