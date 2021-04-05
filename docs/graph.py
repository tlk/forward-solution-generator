#!/usr/bin/env python3
import itertools

pocket = bytes.fromhex("071928364c52637d8896a7b9c3ddecf2")

color_palette = ["#72e5ef", "#fb2076", "#69ef7b", "#f365e7",
                 "#54a32f", "#bf9fff", "#c0e15c", "#753fc2",
                 "#e78607", "#8a0458", "#1c5e39", "#e46981",
                 "#509f87", "#db3c18", "#18519b", "#f2d174"]

def value_format(val):
    return f"{val:02x}"

def edge_color(val):
    index = pocket.index(val)
    return color_palette[index]

def render_graph():
    print('strict digraph {')
    print('layout=circo pad=0.2 mindist=1.8')

    for value, color in zip(pocket, color_palette):
        print(f'"{value_format(value)}" [style="filled" fillcolor="{color}" color="{color}" fontcolor="{color}"]')

    for x, y, z in itertools.product(pocket, repeat=3):
        xor_value = value_format(x ^ y ^ z)
        print(f'"{value_format(x)}" -> "{xor_value}" [arrowsize=0.4 color="{edge_color(x)}"];')
        print(f'"{value_format(y)}" -> "{xor_value}" [arrowsize=0.4 color="{edge_color(y)}"];')
        print(f'"{value_format(z)}" -> "{xor_value}" [arrowsize=0.4 color="{edge_color(z)}"];')

    print('}')

if __name__ == "__main__":
    render_graph()
