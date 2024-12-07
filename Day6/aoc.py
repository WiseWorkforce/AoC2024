import sys
import os
import copy
import time

start_time = time.time()
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc

def replace_char_in_str(input_str, value_to, idx):
    return input_str[:idx] + value_to + input_str[idx+1:]

def get_start_position(input):
    row_num = 0
    while row_num < len (input):
        col_num = 0
        while col_num < len(input[row_num][0]):
            if input[row_num][0][col_num] == "^":
                return [row_num, col_num]
            col_num += 1
        row_num += 1
    return False

input_test, input_real = aoc.getInput(current)

input = input_real
#input = input_test

original_input = copy.deepcopy(input)

vertical = {"^" : -1, "v" : 1}
horizontal = {"<" : -1, ">" : 1}
direction_to = {"^" : ">" , ">" : "v", "v" : "<", "<" : "^"}

def part1(input, check_for_loop = False, max_steps = 0):
    start_position = get_start_position(input)
    direction = input[start_position[0]][0][start_position[1]]
    first_row, first_col = [start_position[0], start_position[1]]
    initial_direction = direction
    loop = False
    steps_taken = 0
    while True:
        if check_for_loop:
            if steps_taken > max_steps:
                loop = True
                break
        if direction in vertical.keys():
            new_row = start_position[0] + vertical[direction]
            new_col = start_position[1]
            char_to_place = "|"
        if direction in horizontal.keys():
            new_row = start_position[0]
            new_col = start_position[1] + horizontal[direction]
            char_to_place = "-"
        if input[start_position[0]][0][start_position[1]] == "+":
            char_to_place = "+"
        # end of grid (vertically, down)
        if new_row >= len(input):
            input[start_position[0]][0] = replace_char_in_str(input[start_position[0]][0], "|", start_position[1])
            break
        # end of grid (vertically, up)
        if new_row < 0:
            input[start_position[0]][0] = replace_char_in_str(input[start_position[0]][0], "|", start_position[1])
            break
        # end of grid (horizontally
        if new_col >= len(input[0][0]):
            input[start_position[0]][0] = replace_char_in_str(input[start_position[0]][0], "-", start_position[1])
            break
        # end of grid (horizontally
        if new_col < 0:
            input[start_position[0]][0] = replace_char_in_str(input[start_position[0]][0], "-", start_position[1])
            break
        # Next step is free, just go there
        if input[new_row][0][new_col] == "." or input[new_row][0][new_col] == "-" or input[new_row][0][new_col] == "|":
            input[new_row][0] = replace_char_in_str(input[new_row][0], direction, new_col)
            input[start_position[0]][0] = replace_char_in_str(input[start_position[0]][0], char_to_place, start_position[1])
        # When the next step is a block, turn the direction right
        if input[new_row][0][new_col] == "#" or input[new_row][0][new_col] == "O":
            input[start_position[0]][0] = replace_char_in_str(input[start_position[0]][0], "+", start_position[1])
            direction = direction_to[direction]
            new_row, new_col = start_position    
        start_position = [new_row, new_col]
        steps_taken += 1
    input[first_row][0] = replace_char_in_str(input[first_row][0], initial_direction, first_col)
    return [input, loop]

def get_num_of_steps(input):
    xs = 0
    for row in input:
        xs += row[0].count("-")
        xs += row[0].count("|")
        xs += row[0].count("+")
        xs += row[0].count("^")
    return xs

walked_path, loop = part1(input)
pt1 = get_num_of_steps(walked_path)
runtime = (time.time() - start_time)*1000
print("The outcome of part one is: " + str(pt1))
print("Runtime part one (ms): " +str(runtime))

num_of_blocks = 0
height = len(original_input)
width = len(original_input[0][0])
for row in original_input:
    num_of_blocks += row[0].count("#")
max_steps = (height * width) - num_of_blocks

i = 0
blocked = 0
while i < pt1:
    input_to_check = copy.deepcopy(original_input)
    row_num = 0
    positions_tried = 0
    while row_num < len(input):
        col_num = 0
        stop = False
        while col_num < len(input[row_num][0]):
            char = input[row_num][0][col_num]
            if char == "+" or char == "-" or char == "|":
                positions_tried += 1
                if i+1 == positions_tried:
                    input_to_check[row_num][0] = replace_char_in_str(input_to_check[row_num][0], "O", col_num)
                    stop = True
                    break
            col_num += 1
        if stop:
            break
        row_num += 1   
    walked_path, loop = part1(input_to_check, True, 5500)
    if loop:
        blocked += 1
    #print(str(i) + "/" + str(pt1) + " -- loop: " + str(loop))
    i += 1       
runtime = (time.time() - start_time)*1000
print("The outcome of part two is: " + str(blocked))
print("Runtime part one (ms): " +str(runtime))