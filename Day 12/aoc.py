import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc

input_test, input_real = aoc.getInput2(current)

input = input_real
#input = input_test

visited = [(0,0)]
visited_dict = {}
region_id = 0
cols_checked = []

def check_neighbor(input, coord):
    global region_id
    global cols_checked
    max_col = len(input[0])-1
    max_row = len(input)-1
    r, c = coord
    chr_to_check = input[r][c]
    if region_id not in visited_dict:
        region_id += 1
        visited_dict[region_id] = []
    if c > 0:
        if input[r][c-1] == chr_to_check:
            if (r,c-1) not in visited:
                cols_checked[r] += 1
                visited.append((r,c-1))
                visited_dict[region_id].append((r,c-1))
                check_neighbor(input, (r,c-1))
    if c < max_col:
        if input[r][c+1] == chr_to_check:
            if (r,c+1) not in visited:
                cols_checked[r] += 1
                visited.append((r,c+1))
                visited_dict[region_id].append((r,c+1))
                check_neighbor(input, (r,c+1))
    if r > 0:
        if input[r-1][c] == chr_to_check:
            if (r-1,c) not in visited:
                cols_checked[r-1] += 1
                visited.append((r-1,c))
                visited_dict[region_id].append((r-1,c))
                check_neighbor(input, (r-1,c))
    if r < max_row:
        if input[r+1][c] == chr_to_check:
            if (r+1,c) not in visited:
                cols_checked[r+1] += 1
                visited.append((r+1,c))
                visited_dict[region_id].append((r+1,c))
                check_neighbor(input, (r+1,c))
    return True

def get_area(input):
    global cols_checked
    global region_id
    input = [[y for y in x] for x in input]
    num_rows, num_cols = len(input), len(input[0])
    num_cells = num_cols * num_rows
    visited_dict[0] = [(0,0)]
    cols_checked = [0 for x in range(num_cols)]
    cols_checked[0] = 1
    while len(visited) < num_cells:
        if len(visited) == 1:
            coord = (0,0)
            r = check_neighbor(input, coord)
        else:
            for i, row in enumerate(input):
                if cols_checked[i] < num_cols:
                    for j, chr in enumerate(row):
                        if (i,j) not in visited:
                            region_id += 1
                            visited_dict[region_id] = [(i,j)]
                            visited.append((i,j))
                            cols_checked[i] += 1
                            r = check_neighbor(input, (i,j))
    return visited_dict

def count_fences(coords, max_row, max_col):
    fences = 0
    for coord in coords:
        r,c = coord
        if r == 0: # Outer limits, always a fence
            fences += 1
        if r == max_row:
            fences += 1
        if c == 0:
            fences += 1
        if c == max_col:
            fences += 1
        if r < max_row:
            if (r+1,c) not in coords: # row below not present, fence at bottom
                fences += 1
        if r > 0:
            if (r-1,c) not in coords: # row above not present, fence at top
                fences += 1
        if c < max_col:
            if (r, c+1) not in coords:
                fences += 1
        if c > 0:
            if (r,c-1) not in coords:
                fences += 1
    return fences

def get_corners(coords):
    corners = 0
    for coord in coords:
        r,c = coord
        # outside corner left-top
        if (r,c-1) not in coords and (r-1,c) not in coords:
            corners +=1
        # outside corner right-top
        if (r,c+1) not in coords and (r-1,c) not in coords:
            corners +=1
        # outside corner left-bottom
        if (r,c-1) not in coords and (r+1,c) not in coords:
            corners +=1
        # outside corner right-bottom
        if (r,c+1) not in coords and (r+1,c) not in coords:
            corners +=1
        # inside corner top right
        if (r-1,c) in coords and (r-1,c+1) not in coords and (r,c+1) in coords:
            corners +=1
        # inside corner top left
        if (r-1,c) in coords and (r-1,c-1) not in coords and (r,c-1) in coords:
            corners +=1
        # inside corner bottom left
        if (r,c-1) in coords and (r+1,c-1) not in coords and (r+1,c) in coords:
            corners +=1
        # inside corner bottom right
        if (r,c+1) in coords and (r+1,c+1) not in coords and (r+1,c) in coords:
            corners +=1
    return corners

def partone(input):
    max_col = len(input[0])-1
    max_row = len(input)-1
    a = get_area(input)
    print(a)
    outcome = 0
    for r in a:
        area = len(a[r])
        coords = a[r]
        f = count_fences(coords, max_row, max_col)
        outcome += area * f
    print(outcome)


def parttwo(input):
    max_col = len(input[0])-1
    max_row = len(input)-1
    a = get_area(input)
    outcome = 0
    for r in a:
        area = len(a[r])
        coords = a[r]
        c = get_corners(coords)
        outcome += area * c
    print(outcome)

#partone(input)  
parttwo(input)