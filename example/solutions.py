from lib import nforward_unrolled
from lib import nreverse

target = "Hello there!!!!\0"
count = 0

for solution in nreverse.reverse(target):
    hex_solution = ",".join(f"0x{c:02x}" for c in solution)
    print(f"{count:08n}", hex_solution, "\t", nforward_unrolled.forward(solution))
    count += 1
