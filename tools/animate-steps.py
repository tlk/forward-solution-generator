#!/usr/bin/env python3
import itertools, os, sys
from PIL import Image, ImageOps
from game import nforward_unrolled, utils

def usage():
    message = """
    Animate the SP-network in 256 steps. The result is an animated gif file.
    Example usage: echo 0x4d7984e3ddaf93d78ea76f8ca0c1465fdb6065016b19e9d2ceff50adca9c85d4 | animate-steps.py [output.gif]
    """
    print(message, file=sys.stderr)
    sys.exit(1)

def make_animation(fd, round_data, rounds=256, fps=10):
    width = len(round_data) * 8
    height = rounds + 1

    frames = []
    rows = []
    rows.append(round_data)

    for frame_index in range(height):

        if frame_index > 0:
            round_data = nforward_unrolled.permute(nforward_unrolled.substitute(round_data))
            rows.append(round_data)

        bitmap_data = bytes(itertools.chain.from_iterable(rows))
        bitmap_image = Image.frombuffer(mode="1", size=(width, len(rows)), data=bitmap_data, decoder_name="raw")
        colorized_bitmap = ImageOps.colorize(image=bitmap_image.convert(mode="L"), black=(0,0,0xff), white=(0,0xff,0))

        frame = Image.new(mode="RGBA", size=(width, height), color=(0xff,0xff,0xff))
        frame.paste(colorized_bitmap)

        frames.append(frame)
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

    """
    Read a single line from stdin.
    """
    data = next(sys.stdin)

    solution = utils.parse_solution(data)
    make_animation(fd, solution)
