import numpy as np
import re

def repeating_pattern(number):
    s = str(number)
    found_sequences = []
    max_len_to_check = len(s) // 2

    # Iterate through all possible sequence lengths (k)
    for k in range(1, max_len_to_check + 1):
        
        # pattern = r"^(\d{" + str(k) + r"})" + r"\1{1}$" # regex for exactly 2 repeats
        pattern = r"^(\d{" + str(k) + r"})" + r"\1+$" # regex for n repeats
        
        # Use re.findall to find all occurrences of this pattern
        # findall with a capturing group returns only the captured group content
        matches = re.findall(pattern, s)
        
        # Add all unique matches to the set
        for match in matches:
            found_sequences.append(match)
    if len(found_sequences) == 0:
        return False
    else:
        return True

with open("day2/day2_ids.txt") as f:
    id_ranges = f.readline().split(",")

r_holder = []
for ids in id_ranges:
    r = ids.split("-")
    r_l, r_u = [int(x) for x in r]

    for num in range(r_l, r_u+1):
        if repeating_pattern(num):
            r_holder.append(num)

print(r_holder)
print(sum(r_holder))


