#!/usr/bin/env python3
import itertools
from docs import εὕρηκα

def render_html(𝛹):
    render_header()

    print("""
        <h1>Definition of sets that are cyclic under ternary XOR</h1>

        <p>Let us define a set to be cyclic under ternary XOR when XOR'ing any
        three numbers from the set results in a new number that belongs to the
        set itself.</p>

        <pre>""")

    render_file("docs/definition.py")

    print("""</pre>

        <p>If there exists a non-empty set 𝛹 that satisfies the
        <code>is_cyclic_under_ternary_xor</code> definition given above, what
        happens if we XOR more than three numbers from 𝛹?</p>

        <p>Let us XOR 𝑎, 𝑏, 𝑐, 𝑑, 𝑒 from 𝛹. We do this by first XOR'ing 𝑎, 𝑏, 𝑐
        to get 𝑥, and then XOR 𝑥 with the remaining 𝑑, 𝑒. We know by definition
        that 𝑎 ⊕ 𝑏 ⊕ 𝑐 = 𝑥 and that 𝑥 belongs to 𝛹. Since 𝑥, 𝑑, 𝑒 all belong to
        𝛹, the result of 𝑥 ⊕ 𝑑 ⊕ 𝑒 also belongs to 𝛹. So it turns out that when
        𝑎, 𝑏, 𝑐, 𝑑, 𝑒 all belong to 𝛹 then the result of 𝑎 ⊕ 𝑏 ⊕ 𝑐 ⊕ 𝑑 ⊕ 𝑒
        belongs to 𝛹.

        <p>This process can be repeated for 𝑛 numbers from 𝛹 where 𝑛 ≥ 3 and 𝑛
        is odd.</p>

        <p>It follows by induction that: if 𝑥 is the result of XOR'ing 𝑛
        numbers from 𝛹 where 𝑛 ≥ 3 and 𝑛 is odd, then 𝑥 itself is a member of
        𝛹.</p>


        <h1>Visualization of a set that is cyclic under ternary XOR</h1>

        <p>The following tables illustrate all 16³ combinations of 𝑎 ⊕ 𝑏 ⊕ 𝑐
        for 𝑎, 𝑏, 𝑐 in 𝛹' where 𝛹' is a set of 16 carefully selected
        numbers.</p>

        <p>Each number in 𝛹' has been assigned a unique color. The set is also
        illustrated by a colored graph under the tables.</p>
        """)

    render_tables(𝛹)
    render_file("docs/graph.svg")
    render_footer()

def render_header():
    color_palette = ["#72e5ef", "#fb2076", "#69ef7b", "#f365e7",
                     "#54a32f", "#bf9fff", "#c0e15c", "#753fc2",
                     "#e78607", "#8a0458", "#1c5e39", "#e46981",
                     "#509f87", "#db3c18", "#18519b", "#f2d174"]

    print("<html>")
    print("<header>")
    print("<style>")
    print("table { display: inline-block }")
    print("td, th.hilite { background-color: currentcolor }")
    for index, css_color in enumerate(color_palette):
        css_class = f".idx_{index}"
        print(css_class, "{color:", css_color, "}")
    print("</style>")
    print("<meta charset=utf-8></header><body>")

def render_footer():
    print("/* Adjusted color palette from")
    print("<a href=http://vrl.cs.brown.edu/color>Colorgorical</a> */")
    print("</body>")
    print("</html>")

def render_file(filename):
    with open(filename) as f:
        print(f.read())

def render_tables(𝛹):
    cols = 4
    print("<table>")
    for index, number in enumerate(𝛹):
        if index % cols == 0:
            print("<tr>")

        print("<td>")
        render_table(𝛹, number)
        print("</td>")

        if index % cols == (cols - 1):
            print("</tr>")

    print("</table>")

def render_table(𝛹, 𝑎):
    def hex_format(𝑥):
        return f"{𝑥:02x}"

    def css_class(𝑥):
        return "idx_" + str(𝛹.index(𝑥))

    print("<table>")

    print(f"<tr><th class='{css_class(𝑎)} hilite'>{hex_format(𝑎)}</th>")
    for 𝑏 in 𝛹:
        print(f"<th class={css_class(𝑏)}>{hex_format(𝑏)}</th>")
    print("</tr>")

    for 𝑏 in 𝛹:
        print(f"<tr><th class={css_class(𝑏)}>{hex_format(𝑏)}</th>")
        for 𝑐 in 𝛹:
            𝑥 = 𝑎 ^ 𝑏 ^ 𝑐
            print(f"<td class={css_class(𝑥)}>{hex_format(𝑥)}</td>")
        print("</tr>")

    print("</table>")

if __name__ == "__main__":
    𝛹 = εὕρηκα.get_magic_numbers()
    render_html(𝛹)
