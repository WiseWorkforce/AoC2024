import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc

input_test, input_real = aoc.getInput(current)

input = input_real
# input = input_test

def horizontal(row_lst, word_to_find):
    x = 0
    i = 0
    while i < len(row_lst) -3:
        chr = row_lst[i]
        if chr == word_to_find[0:1]:
            str_to_check = chr + row_lst[i+1] + row_lst[i+2] + row_lst[i+3]
            if str_to_check == word_to_find:
                x += 1
        i +=1
    return x

def diagonal(input, word_to_find, inverse = False):
    if inverse:
        input = input[::-1]
    row_num = 0
    x = 0
    while row_num < len(input)-3:
        char_num = 0
        while char_num < len(input[row_num][0])-3:
            if input[row_num][0][char_num] == word_to_find[0:1]:
                str_to_check = input[row_num][0][char_num] + input[row_num+1][0][char_num+1] + input[row_num+2][0][char_num+2]+ input[row_num+3][0][char_num+3]
                if str_to_check == word_to_find:
                    x += 1
            char_num +=1
        row_num += 1
    return x

def transpose_input_90(input):
    i = 0
    row_len = len(input[0][0])
    input_transposed = []
    while i < row_len:
        row_str = input[i][0]
        trans_str = ''
        j = 0
        while j < len(row_str):
            trans_str += input[j][0][i]
            j +=1
        input_transposed.append(trans_str)
        i+= 1
    return input_transposed



found = 0
word_to_find = "XMAS"

#
# Horizontal
#
for row in input:
    row_lst = list(row[0])
    # left to right
    found += horizontal(row_lst, word_to_find) #checked = 3
    # right to left
    found += horizontal(row_lst, word_to_find[::-1]) #checked = 2

#
# Vertical
#
    
# transpose the grid to search vertically
input_transposed = transpose_input_90(input)
for row in input_transposed:
    row_lst = list(row)
    # left to right (equals top to bottom)
    found += horizontal(row_lst, word_to_find) #checked = 1
    # right to left (equals bottom to top)
    found += horizontal(row_lst, word_to_find[::-1]) #checked = 2
#
# Diagonal
#

#lefttop to rightbottom
found += diagonal(input, word_to_find) #checked = 1 (9)
#rightbottom to lefttop
found += diagonal(input, word_to_find[::-1]) # checked = 4 (13)
#leftbottom to righttop
found += diagonal(input, word_to_find, True) # checked = 4 (17)
#righttop to leftbottom
found += diagonal(input, word_to_find[::-1], True)
print("The outcome of part one is: " + str(found))

#
#
# Part 2
#
#
xmas = 0
row_num = 1
for row in input[1:-1]:
    row_str = row[0]
    char_position = 1
    for char in row_str[1:-1]:
        if char == "A":
            # check left top char
            lt = input[row_num-1][0][char_position-1]
            rb = input[row_num+1][0][char_position+1]
            rt = input[row_num-1][0][char_position+1]
            lb = input[row_num+1][0][char_position-1]
            lt_rb = lt + char + rb
            rt_lb = rt + char + lb
            if (lt_rb == "MAS" or lt_rb == "SAM") and (rt_lb == "MAS" or rt_lb == "SAM"):
                xmas +=1
        char_position += 1
    row_num += 1
print("The outcome of part one is: " + str(xmas))