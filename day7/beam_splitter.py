import numpy as np

# with open("day7/tachyon_test.txt") as f:
#     rows = f.read().splitlines()

with open("day7/tachyon.txt") as f:
    rows = f.read().splitlines()    

tachyons = np.array([list(r) for r in rows])
print(tachyons)

# PART 1
# splits = 0
# for i, row in enumerate(tachyons):
#     if i == 0:
#         search_val = "S"
#     elif i == len(tachyons) - 1:
#         continue
#     else:
#         search_val = "|"
#     for j, val in enumerate(row):
#         if val == ".":
#             continue
#         elif val == search_val:
#             next_path = tachyons[i+1, j]
#             if next_path == ".":
#                 tachyons[i+1, j] = "|"
#             elif next_path == "^":
#                 tachyons[i+1, j+1] = "|"
#                 tachyons[i+1, j-1] = "|"
#                 splits += 1
# # print(tachyons)
# print(splits)


# PART 2
timelines = {}
start = (0, 0)
for j,val in enumerate(tachyons[0]):
    if val == "S":
        start = (0, j)
        timelines[start] = 1
        break


def explore_path(start):
    prev_timeline_count = timelines.get(start)
    row_num, col_num = start
    current_val = tachyons[row_num+2, col_num]
    if current_val == ".":
        drop_path =(row_num+2, col_num)
        timelines[drop_path] = timelines.get(drop_path, 0) + prev_timeline_count
        return [drop_path]
    else: # current_val == ^
        left_path = (row_num+2, col_num-1)
        timelines[left_path] = timelines.get(left_path, 0) + prev_timeline_count
        right_path = (row_num+2, col_num+1)
        timelines[right_path] = timelines.get(right_path, 0) + prev_timeline_count
        return [left_path, right_path]

row_num = 0
coordinates = start
while row_num < len(tachyons) - 2:
    options_next = []
    if row_num == 0:
        options = [start]
    for option in options:
        options_next += explore_path(option)
    options = list(set(options_next))
    row_num += 2

possibilities = [val for (r, c), val in timelines.items() if r == len(tachyons) - 2]
print(sum(possibilities))

# Expected number of timelines per split:
# .......S.......
# .......|....... 
# ......|^|...... 2 = 1 + 1
# ......|.|...... 
# .....|^|^|..... 4 = 1 + (1 + 1) + 1
# .....|.|.|.....
# ....|^|^|^|.... 8 = 1 + (1 + 2) + (1 + 2) + 1
# ....|.|.|.|....
# ...|^|^|||^|... 13 = 1 + (1 + 3) + 3 + 3 + 1 + 1
# ...|.|.|||.|...
# ..|^|^|||^|^|..
# ..|.|.|||.|.|..
# .|^|||^||.||^|.
# .|.|||.||.||.|.
# |^|^|^|^|^|||^|
# |.|.|.|.|.|||.|