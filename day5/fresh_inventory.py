with open("day5/ingredient_db.txt") as f:
    rows = f.read().splitlines()

# with open("day5/ingredient_db_test.txt") as f:
#     rows = f.read().splitlines()

ranges_str = [x.split("-") for x in rows if "-" in x ]
ranges = [[int(x),int(y)] for x,y in ranges_str]
ids_to_check = [int(x) for x in rows if ("-" not in x and x.isdigit and x != "")]
print(ranges, ids_to_check)

# PART 1
tracker = 0
for i in ids_to_check:
    for r in ranges:
        if r[0] <= i <= r[1]:
            tracker += 1
            break
print(tracker)

# PART 2
ranges.sort(key=lambda x: x[0]) # sort by ascending range start number
tracker: list[list] = []
for i, r in enumerate(ranges):
    r_lower, r_upper = r
    print(f"Processing range {r_lower} <-> {r_upper}")
    merge = False
    if i ==0:
        tracker.append([r_lower, r_upper])
    else:
        t_lower, t_upper = tracker[-1]
        # track valid ranges, merging if overlap
        if t_lower <= r_lower <= t_upper:
            if r_upper >= t_upper:
                tracker[-1][1] = r_upper # extend range
            elif t_lower <= r_upper <= t_upper:
                continue # already encompassed in another range
        else:
            # not covered so add new range
            tracker.append([r_lower, r_upper])
print(tracker)

counter = 0
for t_0, t_1 in tracker:
    counter += t_1+1-t_0
print(counter)
