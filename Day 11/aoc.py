import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc

input_test, input_real = aoc.getInput2(current)

input = input_real
#input = input_test

stones = [x.split(' ') for x in input][0]


def brute_force(stones, blinks):
    step = stones
    i = 0
    while i < blinks:
        print(i)
        row_line = []
        for stone in step:
            if stone == "0":
                row_line.append("1")
            elif len(stone) % 2 == 0:
                firstpart, secondpart = stone[:len(stone)//2], stone[len(stone)//2:]
                row_line.append(str(int(firstpart)))
                row_line.append(str(int(secondpart)))
            else:
                calc = int(stone) * 2024
                row_line.append(str(calc))
        step = row_line
        i += 1
        print(step)
    num_stones = len(step)
    print("stones: " + str(num_stones))

def optimised(stones, blinks):
    stones = [int(x) for x in stones]
    d = {}
    for stone in stones:
        d[stone] = 1
    i = 0
    while i < blinks:
        print(d)
        new_d = {}
        for s in d:
            cnt = d[s]
            if s == 0:
                if 1 in new_d:
                    new_d[1] += cnt
                else:
                    new_d[1] = cnt
            elif len(str(s)) % 2 == 0:
                firstpart, secondpart = int(str(s)[:len(str(s))//2]), int(str(s)[len(str(s))//2:])
                if firstpart in new_d:
                    new_d[firstpart] += cnt
                else:
                    new_d[firstpart] = cnt
                if secondpart in new_d:
                    new_d[secondpart] += cnt
                else:
                    new_d[secondpart] = cnt
            else:
                calc = int(s) * 2024
                if calc in new_d:
                    new_d[calc] += cnt
                else:
                    new_d[calc] = cnt
        d = new_d
        i += 1
    outcome = 0
    for s in d:
        outcome += d[s]
    print (outcome)


#brute_force(stones,25)

optimised(stones,75)

