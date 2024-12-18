import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc

input_test, input_real = aoc.getInputNotSplitted(current)

def get_positions(input):
    pos = []
    for x in input.split("\n"):
        p = x.split(" ")[0][2:].split(",")
        p = [int(x) for x in p]
        pos.append(p)
    return pos    

def get_velocities(input):
    vel = []
    for x in input.split("\n"):
        v = x.split(" ")[1][2:].split(",")
        v = [int(x) for x in v]
        vel.append(v)
    return vel

def make_grid(w, h):
    grid = []
    for i in range(h):
        row = []
        for j in range(w):
            row.append(0)
        grid.append(row)
    return grid

def step(pos,vel,grid):
    h, w = (len(grid), len(grid[0]))
    steps = 100
    for i, p in enumerate(pos):
        j = 0
        # initial position
        #i = 10
        p = pos[i]
        v = vel[i]
        cur_pos = [p[0], p[1]]
        grid[p[1]][p[0]] += 1
        while j < steps:
            x = cur_pos[0] + v[0]
            y = cur_pos[1] + v[1]
            if y < 0:
                y = h + y
            if y >= h:
                y = y - h
            if x < 0:
                x = w + x
            if x >= w:
                x = x - w
            grid[y][x] += 1
            grid[cur_pos[1]][cur_pos[0]] -= 1
            cur_pos = [x,y]
            j += 1
    return grid
    
def split_quadrants(grid):
    h, w = (len(grid), len(grid[0]))
    m_h = int(h / 2)
    m_w = int(w / 2)
    quads = [0,1,2,3]
    for i, q in enumerate(quads):
        quads[i] = []
    q = 0    
    for i, r in enumerate(grid):
        if i != m_h:
            for j, c in enumerate(grid):
                if j == m_w:
                    quads[q].append(r[:m_w])
                    quads[q+1].append(r[m_w+1:])
            if i == m_h-1:
                q += 2
    return quads

def multiply(lst):
    res = 1
    for l in lst:
        res *= l
    return res

def partone(input):
    w = 101
    h = 103
    #w = 11
    #h = 7
    p = get_positions(input)
    v = get_velocities(input)
    grid = make_grid(w,h)
    grid = step(p,v,grid)
    q = split_quadrants(grid)
    s_q = []
    for q in q:
        r_sum = 0
        for r in q:
            r_sum += sum(r)
        s_q.append(r_sum)
    res = multiply(s_q)
    print(res)

input = input_real
#input = input_test


partone(input)