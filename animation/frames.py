import os
import itertools
from lib import nforward
from lib import nreverse

def build(target):
    os.makedirs("build", exist_ok=True)
    generator = nreverse.reverse(target)
    sample_solution = next(generator)
    write_sample_frames(0, sample_solution)

def write_sample_frames(sample_no, start_data):
    rounds = 256
    image_height = rounds + 1
    image_width = 32 * 8
    lines = []
    data = start_data

    for frame in range(image_height):
        filename = f"build/{sample_no:02}_{frame:04}.ppm"
        with open(filename, "wb") as f:
            header = f"P6\n{image_width} {image_height}\n255\n"
            f.write(header.encode('utf-8'))

            draw_line(f, start_data)

            if frame > 0:
                data = nforward.forward_single_round(data)
                lines.append(data)

            for line in lines:
                draw_line(f, line)
            for i in range(image_height - len(lines)):
                draw_white_line(f, image_width)

        print(filename)

def draw_line(f, data):
    for byte in data:
        for bit in range(8):
            if (byte >> (7-bit))&1:
                pixel = [0,0xff,0]
            else:
                pixel = [0,0,0xff]
            f.write(bytearray(pixel))

def draw_white_line(f, width):
    for i in range(width):
        pixel = [0xff,0xff,0xff]
        f.write(bytearray(pixel))

target = "Hello there!!!!\0"
build(target)
