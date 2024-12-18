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

def step(pos,vel,grid, num_steps):
    h, w = (len(grid), len(grid[0]))
    for i, p in enumerate(pos):
        j = 0
        # initial position
        #i = 10
        p = pos[i]
        v = vel[i]
        cur_pos = [p[0], p[1]]
        grid[p[1]][p[0]] += 1
        while j < num_steps:
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

def one_step(pos, vel, grid, prev_pos):
    h, w = (len(grid), len(grid[0]))
    for i, p in enumerate(pos):
        p = pos[i]
        v = vel[i]
        cur_x, cur_y = p
        if len(prev_pos[i]) > 0: # When there was a step before, remove that one first
            grid[prev_pos[i][1]][prev_pos[i][0]] -= 1
        # Place the robot on the positions asked
        grid[cur_y][cur_x] +=1    
        prev_pos[i] = [cur_x, cur_y]
        x = cur_x + v[0]
        y = cur_y + v[1]
        if y < 0:
            y = h + y
        if y >= h:
            y = y - h
        if x < 0:
            x = w + x
        if x >= w:
            x = x - w
        pos[i] = [x,y]
    return pos, vel, grid, prev_pos


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
    grid = step(p,v,grid, 100)
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

def parttwo(input):
    w = 101
    h = 103
    #w = 11
    #h = 7
    p = get_positions(input)
    v = get_velocities(input)
    grid = make_grid(w,h)
    steps = 10000000000
    prev_pos = []
    for i in p:
        prev_pos.append([])
    i = 0
    while i < steps:
        p,v,grid,prev_pos = one_step(p,v,grid, prev_pos)
        unique_rows = 0
        for r in grid:
            t = [str(x) for x in r]
            row_str = ''.join(t).replace("0"," ")
            unique_chars = set(t)
            if len(unique_chars) > 2:
                break
            unique_rows += 1
        if unique_rows == h:
            for r in grid:
                t = [str(x) for x in r]
                print(''.join(t).replace("0"," "))
            print(i)
            break
        i += 1
partone(input)
parttwo(input)