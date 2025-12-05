

with open("day1_rotations.txt") as f:
    rotations_to_do = f.readlines()

new_val = 50
counter = 0
for r in rotations_to_do:
    dir = r[0]
    val = int(r[1:])
    if dir == "L":
        val = -val
    new_val = new_val + val
    if new_val < 0 or new_val >= 100:
        new_val = new_val % 100
    print(new_val, val)
    if new_val == 0:
        counter= counter + 1

print(f"{counter} times reset to 0")