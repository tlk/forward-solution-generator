#!/usr/bin/env python3
import sys, time
from game import nreverse

def usage():
    message = """
    Generate a number of game solutions to stdout.
    Example usage: reverse.py 10 'Hello there!'
    """
    print(message, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":

    try:
        count = int(sys.argv[1])
    except:
        usage()

    if len(sys.argv) > 2:
        target = sys.argv[2]
    else:
        target = "Hello there!!!!\0"

    is_perftest = len(sys.argv) > 3 and sys.argv[3] == "perftest"

    """
    Ensure target length is 16 characters, possibly space-padded.
    """
    target = f"{(target[:16]):<16}"

    """
    Initialize solution generator
    """
    solution_generator = nreverse.reverse(target)

    start = time.time()

    for _ in range(count):
        solution = next(solution_generator)
        print("".join(f"{byte:02x}" for byte in solution))

    end = time.time()

    if is_perftest:
        duration = end - start
        average_time_per_solution_in_ms = (1000 * duration) / count

        print(f"{count} solutions found in {duration:.2f}s, on average {average_time_per_solution_in_ms:.2f}ms per solution.", file=sys.stderr)
