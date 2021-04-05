#!/usr/bin/env python3
import itertools

pocket = bytes.fromhex("071928364c52637d8896a7b9c3ddecf2")

color_palette = ["#72e5ef", "#fb2076", "#69ef7b", "#f365e7",
                 "#54a32f", "#bf9fff", "#c0e15c", "#753fc2",
                 "#e78607", "#8a0458", "#1c5e39", "#e46981",
                 "#509f87", "#db3c18", "#18519b", "#f2d174"]

def render_style():
    print("<style>")
    print("table { display: inline-block }")
    print("td, th.z { background-color: currentcolor }")
    for index, css_color in enumerate(color_palette):
        css_class = f".val{index}"
        print(css_class, "{color:", css_color, "}")
    print("</style>")

def table_class(val):
    return "tbl" + str(pocket.index(val))

def value_class(val):
    return "val" + str(pocket.index(val))

def value_format(val):
    return f"{val:02x}"

def set_format(val):
    return "[" + ", ".join([value_format(x) for x in pocket]) + "]"

def render_table(x):
    print(f"<table class={table_class(x)}>")
    print(f"<tr><th class='{value_class(x)} z'>{value_format(x)}</th>")

    for col_header in pocket:
        col_header_fmt = f"{col_header:02x}"
        print(f"<th class={value_class(col_header)}>{value_format(col_header)}</th>")
    print("</tr>")

    for row in pocket:
        print(f"<tr><th class={value_class(row)}>{value_format(row)}</th>")
        for col in pocket:
            value = x ^ row ^ col
            print(f"<td class={value_class(value)}>{value_format(value)}</td>")
        print("</tr>")

    print("</table>")

def render_graph_svg():
    with open("graph.svg") as f:
        for line in f:
            print(line, end="")

if __name__ == "__main__":
    print("<html>")
    print("<header>")
    render_style()
    print("<meta charset=utf-8>")
    print("</header>")
    print("<body>")

    print("<h1>Cyclic data set under XOR</h1>")
    print("This Python code verifies that XOR'ing any three values from the set R =", set_format(pocket), "results in a value which itself belongs to the set R.<br>")
    print("<pre>")
    with open("proof.py") as f:
        for line in f:
            print(line, end="")
    print("</pre>")
    print("""
        <p>Does this property expand to XOR'ing a larger number of values?
        We can XOR five values from the set R by XOR'ing the first three values
        and take the result of that and XOR it with the remaining two values.
        Now, we know that XOR'ing any three values from the set R results in a
        value that also belongs to the set R. Going back to the task of XOR'ing
        the five values, we now know that the result of the first three-value
        XOR is itself a value from the set R. The remaining two values also
        belong to the set R. In other words, we now have three values from the
        set R and we know that the result of XOR'ing those three values is
        going to belong to the set R.</p>

        <p>This process can be repeated for N values from the set R where N ≥ 3
        and N is odd.</p>

        <p>It follows that: the result of XOR'ing N values from the set R
        where N ≥ 3 and N is odd always Are belong to us. That is, always
        belongs to the set R.</p>

        <p>/tlk</p>
        """)

    print("""
        <h1>Visualizing the data set under XOR</h1>
        <p>The following 16 tables contain all 16³ results of x ⊕ y ⊕ z for x,
        y, z in the set R =""")
    print(set_format(pocket), ".</p>")
    print("""
        <p>Each value in the set R has been assigned a unique color which is
        used to represent the value in the tables.</p>

        <p>The results are also illustrated by a directed graph. Given an edge
        E from node A to node B, the color of node B correponds to an entry in
        the tables. The color of node A correponds to a color in a row, column
        or top-left corner of a table. Edge E has the same color as node A.
        Duplicate edges are not rendered.</p>
        """)

    print("<table>")
    for index, value in enumerate(pocket):
        if index in (0, 4, 8, 12):
            print("<tr>")

        print("<td>")
        render_table(value)
        print("</td>")

    print("</tr>")
    print("</table>")

    render_graph_svg()

    print("/* Adjusted color palette from <a href=http://vrl.cs.brown.edu/color>Colorgorical</a> */")
    print("</body>")
    print("</html>")
