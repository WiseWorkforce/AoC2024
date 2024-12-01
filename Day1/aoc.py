import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc

input_test, input_real = aoc.getInput(current)

input = input_real
#input = input_test


# Part one 

lefts = []
rights = []
for row in input:
    left, right = row[0].split("   ")
    lefts.append(int(left))
    rights.append(int(right))
lefts.sort()
rights.sort()
i = 0
distance = 0
while i < len(lefts):
    distance += abs(lefts[i] - rights[i])
    i += 1
print("The outcome of part one is: " + str(distance))

# Part Two

i = 0
sim_score = 0
while i < len(lefts):
    left = lefts[i]
    num_right = rights.count(left)
    sim_score += left * num_right
    i += 1
print("The outcome of part two is: " + str(sim_score))