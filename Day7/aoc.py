import sys
import os
from multipermute import *
import itertools
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc

input_test, input_real = aoc.getInput(current)

input = input_real
#input = input_test

def split_outcomes_nums(input):
    outcomes = []
    nums = []
    for row in input:
        o = int(row[0].split(":")[0])
        outcomes.append(o)
        n = [int(x) for x in row[0].split(":")[1].split(" ") if x != ""]
        nums.append(n)
    return outcomes,nums

def check_both(values, outcome):
    num_operators = len(values) -1
    num_muls = 0
    for x in range(num_operators+1):
        perms = []
        ops_list = []
        num_muls = num_operators - x
        for y in range(num_muls):
            ops_list.append("*")
        for z in range(num_operators - num_muls):
            ops_list.append("+")
        perms = list(permutations(ops_list))
        for p in perms:
            c = values[0]
            for i in range(len(p)):
                calc_str = str(c) + p[i] + str(values[i+1])
                o = eval(calc_str)
                #print(c, p[i], values[i+1], o)
                c = o
            if c == outcome:

                return True
    return False

def check_tri(values, outcome):
    num_operators = len(values) -1
    combs = list(itertools.combinations_with_replacement(["||","*","+"],num_operators))
    combs2 = []
    for x in combs:
        y = list(permutations(list(x)))
        for a in y:
            combs2.append(a)
    for p in combs2:
        c = values[0]
        for i in range(len(p)):
            if p[i] == "||":
                calc_str = str(c) + str(values[i+1])
            else:
                calc_str = str(c) + p[i] + str(values[i+1])
            o = eval(calc_str)
            c = o
        if c == outcome:
            return True
    return False

def partone(input):
    o, n = split_outcomes_nums(input)
    i = 0
    c = []
    items_to_delete = []
    while i < len(o):
        both = False
        both = check_both(n[i], o[i])
        if both:
            #print(o[i])
            c.append(o[i])
            items_to_delete.append(i)
        i += 1
    for i in range(len(o),-1,-1):
        if i in items_to_delete:
            del o[i]
            del n[i]
    print("The outcome of part one is: " + str(sum(c)))
    return True

def parttwo(input):
    o, n = split_outcomes_nums(input)
    i = 0
    c = []
    while i < len(o):
        print(i)
        tri = False
        tri = check_tri(n[i], o[i])
        if tri:
            c.append(o[i])
        i += 1
    print("The outcome of part two is: " + str(sum(c)))
    return True
#partone(input)

parttwo(input)