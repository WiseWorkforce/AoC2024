import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc

input_test, input_real = aoc.getInput(current)

input = input_real
#input = input_test

def generate_input(input):
    s = []
    prev_empty = 0
    for i, x in enumerate(input):
        if len(x) == 0:
            s.append(input[prev_empty:i])
            prev_empty = i+1
    s.append(input[prev_empty:i+1])
    opts = []
    for o in s: 
        d = {}
        d["AX"] = int(o[0][0].split(": X+")[1])
        d["AY"] = int(o[0][1].split("+")[1])
        d["BX"] = int(o[1][0].split(": X+")[1])
        d["BY"] = int(o[1][1].split("+")[1])
        d["PX"] = int(o[2][0].split("X=")[1])
        d["PY"]= int(o[2][1].split("=")[1])
        opts.append(d)
    return opts

def partone(input):
    costs = 0
    for t in input:
        x_a = t["AX"]
        y_a = t["AY"]
        x_b = t["BX"]
        y_b = t["BY"]
        p_x = t["PX"]
        p_y = t["PY"]
        a = (p_x*y_b - p_y*x_b) / (x_a*y_b - y_a*x_b)
        b = (p_y*x_a - p_x*y_a) / (x_a*y_b - y_a*x_b)
        if a == int(a) and b == int(b):
            costs += (a*3) + b
    print(costs)

def parttwo(input):
    costs = 0
    for t in input:
        x_a = t["AX"]
        y_a = t["AY"]
        x_b = t["BX"]
        y_b = t["BY"]
        p_x = t["PX"] + 10000000000000
        p_y = t["PY"] + 10000000000000
        a = (p_x*y_b - p_y*x_b) / (x_a*y_b - y_a*x_b)
        b = (p_y*x_a - p_x*y_a) / (x_a*y_b - y_a*x_b)
        if a == int(a) and b == int(b):
            costs += (a*3) + b
    print(costs)

input = generate_input(input)
partone(input)
parttwo(input)