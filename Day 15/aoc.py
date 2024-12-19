import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc

input_test, input_real = aoc.getInput(current)

input = input_real
#input = input_test

def parse_input(input):
    for i,r in enumerate(input):
        if len(r) == 0:
            m = input[:i]
            steps = input[i+1:]

    steps = [''.join(x) for x in steps]
    if len(steps) > 0:
        steps = ''.join(steps)
    start = ''
    m = [x[0] for x in m]
    for i,r in enumerate(m):
        for j,c in enumerate(r):
            if c == "@":
                start = (i,j)
    return m, steps, start

def expand_warehouse(m):
    new_chrs = {"#" : "##", "O" : "[]", "." : "..", "@" : "@."} 
    new_m  = []
    for i, r in enumerate(m):
        new_row = []
        for j, c in enumerate(r):
            new_row += new_chrs[c]
        new_m.append(new_row)
    new_m = [''.join(x) for x in new_m]
    for i,r in enumerate(new_m):
        for j,c in enumerate(r):
            if c == "@":
                start = (i,j)
    return new_m, start


def transpose_input_90(input):
    i = 0
    row_len = len(input[0])
    input_transposed = []
    while i < row_len:
        trans_str = ''
        j = 0
        while j < len(input):
            trans_str += input[j][i]
            j +=1
        input_transposed.append(trans_str)
        i+= 1
    return input_transposed


def get_next_pos(pos, d):
    return tuple(map(lambda i,j: i+j, pos, d))

def replace_chr(row, pos, new_chr):
    str_lst = list(row)
    str_lst[pos] = new_chr
    return ''.join(str_lst)

def horizontal_step_with_box(row_str, start_col, direction):
    if direction == ">":
        part_str = row_str[start_col:]
    first_free = part_str.find(".") + start_col
    first_wall = part_str.find("#") + start_col
    if first_wall < first_free or first_free < start_col: # When there's a wall before a free spot, you can't move
        return row_str, start_col
    else: # There's a free spot before a wall, so movement is possible, move all between start_col and first_free on to the direction
        new_str = row_str
        for i in range(first_free, start_col, -1):
            new_str = replace_chr(new_str, i, new_str[i-1])
        new_str = replace_chr(new_str, i-1, ".")
        row_str = new_str
        start_col += 1
    return row_str, start_col

def do_step(m, start, next_pos, direction):
    start_r, start_c = start
    r, c = next_pos
    next_chr = m[r][c]
    if next_chr == "#": # Hits a wall, do nothing, don't move
        return m, start
    elif next_chr == ".": # Next step is free, go to that cell
        m[r] = replace_chr(m[r],c,"@")
        m[start_r] = replace_chr(m[start_r],start_c,".")
        return m, next_pos
    elif next_chr == "O" or next_chr == "]" or next_chr == "[": # Next step is a box
        if direction == ">": # check if there's a free spot to the right
            new_row, c = horizontal_step_with_box(m[start_r], start_c, direction)
            next_pos = (start_r, c)
            m[start_r] = new_row
            return m, next_pos 
        elif direction == "<":
            new_row = m[start_r][::-1] # Inverse the string to move to the right
            direction = ">"
            start_c = len(new_row) - start_c -1 # adjust the start_col for the inversed string
            new_row, c = horizontal_step_with_box(new_row, start_c, direction)
            new_row = new_row[::-1] # Inverse the string back
            c = len(new_row) - c -1 
            next_pos = (start_r, c)
            m[start_r] = new_row
            return m, next_pos
        elif direction == "v":
            initial_m = m[:]
            new_m = []
            for x in range(len(m)-1,-1,-1):
                new_m.append(m[x])
            m = new_m
            start_r, start_c = start
            start_r = len(m) - start_r -1
            boxes = {start_r: [[start_c,start_c]]}
            for i in range(start_r-1,0,-1):
                boxes_below = boxes[i+1]
                new_b = []
                for b in boxes_below: # for every box, check if there's wall above
                    char_above_left = m[i][b[0]]        
                    char_above_right = m[i][b[1]]            
                    if char_above_left != "#" and char_above_right != "#":
                        if char_above_left == "]":
                            new_b.append([b[0]-1,b[0]])
                        if char_above_right == "[":
                            new_b.append([b[1],b[1]+1])
                        if char_above_left == "[":
                            new_b.append([b[0],b[1]])
                boxes[i] = new_b
            # now we have a dict with all the boxes which need moving. Go over them top to bottom, to see if there's a wall blocking
            boxes = dict(sorted(boxes.items()))
            for b in boxes:
                positions = boxes[b]
                if len(positions) > 0:
                    for p in positions:
                        if m[b-1][p[0]] == "." and m[b-1][p[1]] == ".":
                            if m[b][p[0]] == "@":
                                m[b-1] = replace_chr(m[b-1], p[0], "@")
                            else:
                                m[b-1] = replace_chr(m[b-1], p[0], "[")
                                m[b-1] = replace_chr(m[b-1], p[1], "]")
                            m[b] = replace_chr(m[b], p[0], ".")
                            m[b] = replace_chr(m[b], p[1], ".")
                        if m[b-1][p[0]] == "#" or m[b-1][p[1]] == "#":
                            return initial_m, start
            next_pos = (start[0]+1,start_c)
            # turn the grid upside down again
            new_m = []
            for x in range(len(m)-1,-1,-1):
                new_m.append(m[x])
            m = new_m
            return m, next_pos
        elif direction == "^":
            initial_m = m[:]
            start_r, start_c = start
            row_below = start
            boxes = {start_r: [[start_c,start_c]]}
            for i in range(start_r-1,0,-1):
                boxes_below = boxes[i+1]
                new_b = []
                for b in boxes_below: # for every box, check if there's wall above
                    char_above_left = m[i][b[0]]        
                    char_above_right = m[i][b[1]]            
                    if char_above_left != "#" and char_above_right != "#":
                        if char_above_left == "]":
                            new_b.append([b[0]-1,b[0]])
                        if char_above_right == "[":
                            new_b.append([b[1],b[1]+1])
                        if char_above_left == "[":
                            new_b.append([b[0],b[1]])
                boxes[i] = new_b
            # now we have a dict with all the boxes which need moving. Go over them top to bottom, to see if there's a wall blocking
            boxes = dict(sorted(boxes.items()))
            for b in boxes:
                positions = boxes[b]
                if len(positions) > 0:
                    for p in positions:
                        if m[b-1][p[0]] == "." and m[b-1][p[1]] == ".":
                            if m[b][p[0]] == "@":
                                m[b-1] = replace_chr(m[b-1], p[0], "@")
                            else:
                                m[b-1] = replace_chr(m[b-1], p[0], "[")
                                m[b-1] = replace_chr(m[b-1], p[1], "]")
                            m[b] = replace_chr(m[b], p[0], ".")
                            m[b] = replace_chr(m[b], p[1], ".")
                        if m[b-1][p[0]] == "#" or m[b-1][p[1]] == "#":
                            return initial_m, start
            next_pos = (b-1,start_c)
            return m, next_pos


def do_steps(m, steps, start):
    d = {"^" : (-1,0), ">" : (0,1), "v" : (1,0), "<" : (0,-1)}
    pos = start
    for i, s in enumerate(steps):
        print(i,s)
        next_pos = get_next_pos(pos, d[s])
        m, pos = do_step(m, pos, next_pos, s)
    return m

def do_double_steps(m, steps, start):
    d = {"^" : (-1,0), ">" : (0,1), "v" : (1,0), "<" : (0,-1)}
    pos = start
    for i, s in enumerate(steps):
        next_pos = get_next_pos(pos, d[s])
        m, pos = do_step(m, pos, next_pos, s)
    return m

def calculate_coords(m, s):
    score = 0
    for i,r in enumerate(m):
        for j, c in enumerate(r):
            if c == s:
                score += 100 * i + j
    return score

def partone(input):
    m, steps, start = parse_input(input)
    m = do_steps(m, steps, start)
    s = calculate_coords(m, "0")
    print(s)

def parttwo(input):
    m, steps, start = parse_input(input)
    m, start = expand_warehouse(m)
    m = do_double_steps(m, steps, start)
    s = calculate_coords(m, "[")
    print(s)
#partone(input)
parttwo(input)
