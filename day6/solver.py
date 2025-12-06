import numpy as np
import math
import re

with open("day6/homework.txt") as f:
    rows = f.read().splitlines()

# with open("day6/homework_test.txt") as f:
#     rows = f.read().splitlines()


# PART 1
ops = rows[-1].split()
p = np.array([[int(x) for x in r.split()] for r in rows[:-1]])
print(p, ops)

total = 0
for col, op in enumerate(ops):
    if op == "*":
        to_multiply = p[:, col]
        total += math.prod(to_multiply)
    elif op == "+":
        to_add = p[:, col]
        total += sum(to_add)
print(total)

# PART 2
total = 0
ops = np.array(rows[-1].split())
space_sequences = [len(s) for s in re.findall(r'(\s+)', rows[-1])]
print(space_sequences)
p = np.array([list(r) for r in rows[:-1]])
print(p, "\n", ops)

col = 0
for i, op in enumerate(ops):
    r_space = space_sequences[i]
    slice_end = col+r_space
    if i == len(ops) - 1:
        slice_end += 1
    p_target = p[:, col:slice_end]
    to_operate = [int(x) for x in ["".join(columns) for columns in zip(*p_target)]]

    if op == "*":
        total += math.prod([int(x) for x in to_operate])
    elif op == "+":
        total += sum([int(x) for x in to_operate])
    col += r_space + 1
print(total)