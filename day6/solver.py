import numpy as np
import math

with open("day6/homework.txt") as f:
    rows = f.read().splitlines()

# with open("day6/homework_test.txt") as f:
#     rows = f.read().splitlines()

ops = rows[-1].split()
p = np.array([[int(x) for x in r.split()] for r in rows[:-1]])
print(p, ops)

# PART 1
total = 0
for col, op in enumerate(ops):
    if op == "*":
        to_multiply = p[:, col]
        total += math.prod(to_multiply)
    elif op == "+":
        to_add = p[:, col]
        total += sum(to_add)
print(total)
