with open("day1_rotations.txt") as f:
    rotations_to_do = f.readlines()

new_val = 50
counter = 0
for r in rotations_to_do:
    dir = r[0]
    val = int(r[1:])
    if dir == "L":
        val = -val
    old_val = new_val
    new_val = old_val + val

    if new_val >= 100:
        pass_zero_counter = int(new_val/100)
        counter = counter + pass_zero_counter
        new_val = new_val % 100
    elif new_val < 0:
        pass_zero_counter = int(new_val/100)
        if old_val != 0:
            # additional click to 0 on way to negative
            pass_zero_counter = 1-pass_zero_counter
        else:
            # if already on 0, ignore added click to 0 to negative
            pass_zero_counter = -pass_zero_counter
        counter = counter + pass_zero_counter
        new_val = new_val % 100
    
    elif new_val == 0:
        counter= counter + 1

    print(old_val, new_val, val, counter)

print(f"{counter} times reset to 0")