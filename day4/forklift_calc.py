import numpy as np

with open("day4/paper_rolls_map.txt") as f:
    rows = f.read().splitlines()

# with open("day4/paper_rolls_map_test.txt") as f:
#     rows = f.read().splitlines()

# create map matrix
paper_rolls_map = []
for row in rows:
    row_segment = [str(i) for i in row]
    paper_rolls_map.append(row_segment)
paper_rolls_map = np.array(paper_rolls_map)
dim = paper_rolls_map.shape
accessable_roll_count = 0

# PART 1
for i, row in enumerate(paper_rolls_map):
    for j, col in enumerate(row):
        if paper_rolls_map[i,j] == "@":
            # track coordinates of target relative to the grid we are evaluating
            target_pos = [0,0] 
            if i==0:
                target_pos[0] = 0
                i_slice = slice(0, 2)
            elif i == dim[0]-1:
                target_pos[0] = 1
                i_slice = slice(i-1, dim[0])
            else:
                target_pos[0] = 1 
                i_slice = slice(i-1, i+2)
            
            if j==0:
                target_pos[1] = 0
                j_slice = slice(0,2)
            elif j==dim[1]-1:
                target_pos[1] = 1
                j_slice = slice(j-1, dim[1])
            else:
                target_pos[1] = 1
                j_slice = slice(j-1, j+2)
            target_grid = paper_rolls_map[i_slice, j_slice].copy()
            target_grid[target_pos[0], target_pos[1]] = "x"
            print(target_grid)
            targets_to_eval = target_grid.flatten()
            adjacent_roll_count = np.count_nonzero(targets_to_eval == "@")

            if adjacent_roll_count < 4:
                accessable_roll_count = accessable_roll_count + 1
print(accessable_roll_count)


# PART 2

new_map = paper_rolls_map.copy()
finished = False
total_removed_rolls = 0
while finished == False:
    removed_rolls=0
    accessable_roll_count = 0
    old_map = new_map.copy()
    for i, row in enumerate(old_map):
        for j, col in enumerate(row):
            if old_map[i,j] == "@":
                # track coordinates of target relative to the grid we are evaluating
                target_pos = [0,0] 
                if i==0:
                    target_pos[0] = 0
                    i_slice = slice(0, 2)
                elif i == dim[0]-1:
                    target_pos[0] = 1
                    i_slice = slice(i-1, dim[0])
                else:
                    target_pos[0] = 1 
                    i_slice = slice(i-1, i+2)
                
                if j==0:
                    target_pos[1] = 0
                    j_slice = slice(0,2)
                elif j==dim[1]-1:
                    target_pos[1] = 1
                    j_slice = slice(j-1, dim[1])
                else:
                    target_pos[1] = 1
                    j_slice = slice(j-1, j+2)
                target_grid = old_map[i_slice, j_slice].copy()
                target_grid[target_pos[0], target_pos[1]] = "x"

                targets_to_eval = target_grid.flatten()
                adjacent_roll_count = np.count_nonzero(targets_to_eval == "@")

                if adjacent_roll_count < 4:
                    accessable_roll_count += 1
                    new_map[i,j] = "x"
                    removed_rolls += 1
    print(f"Removed roll count: {removed_rolls}")
    total_removed_rolls += removed_rolls
    if removed_rolls == 0:
        finished = True
print(f"Total removed rolls: {total_removed_rolls}")