#!/usr/bin/env python3
import itertools, os, sys
from PIL import Image, ImageOps
from game import nforward_unrolled, utils

def usage():
    message = """
    Animate a stream of 32 byte data values as they are being processed by the SP-network. The result is an animated gif file.
    A single frame show the 256 steps for a single 32 byte data value.
    Example usage: echo 0x4d7984e3ddaf93d78ea76f8ca0c1465fdb6065016b19e9d2ceff50adca9c85d4 | animate-solutions.py [output.gif]
    """
    print(message, file=sys.stderr)
    sys.exit(1)

def make_animation(fd, values, rounds=256, fps=20):
    frames = []

    for round_data in values:
        width = len(round_data) * 8
        height = rounds + 1
        rows = []
        rows.append(round_data)

        for _ in range(rounds):
            round_data = nforward_unrolled.permute(nforward_unrolled.substitute(round_data))
            rows.append(round_data)

        bitmap_data = bytes(itertools.chain.from_iterable(rows))
        bitmap_image = Image.frombuffer(mode="1", size=(width, height), data=bitmap_data, decoder_name="raw")
        colorized_bitmap = ImageOps.colorize(image=bitmap_image.convert(mode="L"), black=(0,0,0xff), white=(0,0xff,0))

        frames.append(colorized_bitmap)
        print(".", end="", flush=True, file=sys.stderr)

    print(".", file=sys.stderr)

    duration = 1000 // fps
    image = frames[0]
    image.save(fd, "gif", save_all=True, append_images=frames[1:], duration=duration, loop=0)
    fd.close()

if __name__ == "__main__":

    if len(sys.argv) == 2:
        fd = open(sys.argv[1], "wb")
    elif not sys.stdout.isatty():
        fd = sys.stdout.buffer
    else:
        usage()

    solutions = [utils.parse_solution(line) for line in sys.stdin]
    make_animation(fd, solutions)
