#!/usr/bin/env python3
from game import ngame

print('digraph {')
print('graph [pad="2", nodesep="5", ranksep="10"];')

for j in range(32):
    for k in range(32):
        if ((ngame.pbox[j]>>k)&1):
            print(f'c{j} -> d{k};')

print('}')
