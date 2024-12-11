import sys
import os
import itertools
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc

input_test, input_real = aoc.getInput(current)

input = input_real
#input = input_test

def get_freqs(input):
    uc = []
    for row in input:
        uc_row = list(set(list(row[0])))
        for c in uc_row:
            if c not in uc and c != ".":
                uc.append(c)
    return uc


def get_rows_with_freq(freq, input):
    rc = []
    i = 0
    while i < len(input):
        row_lst = list(input[i][0])
        if freq in row_lst:
            r = i
            j = 0
            while j < len(row_lst):
                if freq == row_lst[j]:
                    rc.append((i,j))
                j += 1
        i +=1
    return rc

def partone(input):
    freqs = get_freqs(input)
    pos = []
    for freq in freqs:
        freq_pos = get_rows_with_freq(freq, input)
        combs = list(itertools.combinations(freq_pos,2))
        for p in combs:
            r_up = p[0][0] + (p[0][0] - p[1][0])
            c_up = p[0][1] + (p[0][1] - p[1][1])
            pos_up = [r_up, c_up]
            r_down = p[1][0] + (p[1][0] - p[0][0])
            c_down = p[1][1] + (p[1][1] - p[0][1])
            pos_down = [r_down, c_down]
            if pos_up not in pos:
                if pos_up[0] >= 0 and pos_up[0] < len(input) and pos_up[1] >= 0 and pos_up[1] < len(input[0][0]):
                    pos.append(pos_up)
            if pos_down not in pos:
                if pos_down[0] >= 0 and pos_down[0] < len(input) and pos_down[1] >= 0 and pos_down[1] < len(input[0][0]):
                    pos.append(pos_down)
    print("The outcome of part one is: " + str(len(pos)))

def is_in_grid(grid, p):
    if p[0] >= 0 and p[0] < len(grid) and p[1] >=0 and p[1] < len(input[0][0]):
        return True
    return False
    
def parttwo(input):
    freqs = get_freqs(input)
    pos = set()
    pos2 = []
    for freq in freqs:
        freq_pos = get_rows_with_freq(freq, input)
        combs = list(itertools.permutations(freq_pos,2))
        for p in combs:
            diff_r_down = p[1][0] - p[0][0]
            diff_c_down = p[1][1] - p[0][1]
            r_down = p[0][0] + diff_r_down
            c_down = p[0][1] + diff_c_down
            pos_down = (r_down, c_down)
            while is_in_grid(input, pos_down):
                pos.add(pos_down)
                pos2.append(pos_down)
                pos_down = (pos_down[0] + diff_r_down, pos_down[1] + diff_c_down)
    print("The outcome of part two is: " + str(len(pos)))

parttwo(input)