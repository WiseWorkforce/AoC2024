import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc

input_test, input_real = aoc.getInput2(current)

input = input_real
#input = input_test

score = {}

def get_next_location(s_loc, direction):
    if direction == "up":
        n_loc = (s_loc[0]-1, s_loc[1])
    elif direction == "down":
        n_loc = (s_loc[0]+1, s_loc[1])
    elif direction == "left":
        n_loc = (s_loc[0], s_loc[1]-1)
    elif direction == "right":
        n_loc = (s_loc[0], s_loc[1]+1)
    return n_loc

def get_next_step(s_loc, input, num_to_check, start_back = True):
    if start_back:
        chk = num_to_check-1
    else:
        chk = num_to_check + 1
    max_row = len(input)-1
    max_col = len(input[0])-1
    is_endpoint = False
    possible_direction = []
    row_num, col_num = s_loc
    chr = input[row_num][col_num]
    if chr == str(num_to_check):
        # Vertical check
        if row_num >= 0 and row_num <= max_row:
            # Check row above
            if row_num > 0:
                if input[row_num-1][col_num] == str(chk):
                    possible_direction.append("up")
                    is_endpoint = True
            # Check row below
            if row_num < max_row:
                if input[row_num+1][col_num] == str(chk):
                    possible_direction.append("down")
                    is_endpoint = True
        # Horizontal check
        if col_num >= 0 and col_num <= max_col:
            # Check column left
            if col_num > 0:
                if input[row_num][col_num-1] == str(chk):
                    possible_direction.append("left")
                    is_endpoint = True
            # Check column right
            if col_num < max_col:
                if input[row_num][col_num+1] == str(chk):
                    possible_direction.append("right")
                    is_endpoint = True
    if is_endpoint:
        return (row_num, col_num, possible_direction, chk)
    return False

def get_possible_endpoints(input, num_to_check):
    possible_endpoints = []
    for row_num, row in enumerate(input):
        for col_num, chr in enumerate(row):
            r = get_next_step((row_num, col_num),input,num_to_check)
            if r:
                possible_endpoints.append(r)
    return possible_endpoints

def go_over_directions(s_loc, direction, num_to_check, ep_save):
    global score
    n_loc = get_next_location(s_loc, direction)
    step = get_next_step(n_loc, input, num_to_check)
    #print((s_loc, direction, num_to_check), step)
    if step and num_to_check > 0:
        for d in step[2]:
            go_over_directions(n_loc, d, step[3], ep_save)
    elif not step and num_to_check == 0:
        if n_loc in score:
            score[n_loc].append(ep_save)
        else:
            score[n_loc] = [ep_save]
        return True
    return False

def get_unique_routes(end_points, input):
    for ep in end_points:
        #print("---- Endpoint ", ep, "---")
        ep_save = (ep[0],ep[1])
        s_loc = ep[0:2]
        directions = ep[2]
        num_to_check = ep[3]
        for d in directions:
            go_over_directions(s_loc, d, num_to_check, ep_save)

def partone(input):
    end_points = get_possible_endpoints(input, 9)
    get_unique_routes(end_points, input)
    outcome = 0
    for z in score:
        unique = set(score[z])
        outcome += len(unique)
    print(outcome)

def parttwo(input):
    end_points = get_possible_endpoints(input, 9)
    get_unique_routes(end_points, input)
    outcome = 0
    for z in score:
        outcome += len(score[z])
    print(outcome)

parttwo(input)