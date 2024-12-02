import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc

input_test, input_real = aoc.getInput(current)

input = input_real
#input = input_test

def is_desc(lst):
    for x in range(1, len(lst)):
        if lst[x] >= lst[x-1]:
            return False
    return True
    
def is_asc(lst):
    for x in range(1, len(lst)):
        if lst[x] <= lst[x-1]:
            return False
    return True

def is_safe(row):
    direction = None
    if is_desc(row):
        direction = "DESC"
    elif is_asc(row):
        direction = "ASC"
    if direction:
        subs = row[1:]
        diffs = [abs(x-y) for x,y in zip(row, subs)]
        if max(diffs) <= 3:
            return True
    return False

counter = 0

for row in input:
    direction = None
    row_int = [int(x) for x in row[0].split(' ')]
    desc = is_desc(row_int)
    if is_desc(row_int):
        direction = "DESC"
    elif is_asc(row_int):
        direction = "ASC"
    if direction:
        subs = row_int[1:]
        diffs = [abs(x-y) for x,y in zip(row_int, subs)]
        if max(diffs) <= 3:
            counter +=1
print("The outcome of part one is: " + str(counter))

counter = 0

for row in input:
    row_int = [int(x) for x in row[0].split(' ')]
    if is_safe(row_int):
        counter +=1
    else:
        i = 0
        while i < len(row_int):
            new_list = [y for x, y in enumerate(row_int) if x not in [i]] # remove an element from the list and test if it's safe
            if is_safe(new_list):
                counter +=1
                break
            i += 1
print("The outcome of part two is: " + str(counter))