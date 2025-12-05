with open("day3/joltage.txt") as f:
    battery_banks = f.read().splitlines()

### PART 1
max_bank = []
for bank in battery_banks:
    battery_levels = [int(i) for i in bank]
    c = []
    for i, b_0 in enumerate(battery_levels):
        other_levels = battery_levels[i+1:]
        if len(other_levels) == 0:
            continue
        b_1 = max(other_levels)
        c.append(int(str(b_0) + str(b_1)))
    max_bank.append(max(c))
print(max_bank)
print(sum(max_bank))


### PART 2
max_bank = []
for j, bank in enumerate(battery_banks):
    battery_levels = [int(i) for i in bank]
    start_i = 0
    result = []
    print(f"bank num {j}")

    # [1,6,5,9,7]
    for i in range(12):
        endpoint = len(battery_levels)-(12-len(result))+1
        other_levels = battery_levels[start_i: endpoint]
        b_next = max(other_levels)
        next_i = battery_levels.index(b_next, start_i, endpoint)
        start_i = next_i + 1
        result.append(b_next)


    max_value = int("".join(map(str, result)))
    print(f"Max joltage {max_value}")
    max_bank.append(max_value)
print(max_bank)
print(sum(max_bank))