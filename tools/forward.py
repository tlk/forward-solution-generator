#!/usr/bin/env python3
import sys
from game import nforward_unrolled, utils

def usage():
    message = """
    Process game solutions from stdin.
    Example usage: echo 0x4d7984e3ddaf93d78ea76f8ca0c1465fdb6065016b19e9d2ceff50adca9c85d4 | forward.py
    """
    print(message, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) != 1:
        usage()

    for line in sys.stdin:
        solution = utils.parse_solution(line)
        print(line.strip(), nforward_unrolled.forward(solution))
