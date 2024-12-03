import sys
import os
import re
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc


def split_string(input, delimiter):
    return input.split(delimiter)

def part1(input):
    split1 = split_string(input, "mul(")
    split2 = [split_string(x, ")") for x in split1]
    split3 = [split_string(x[0], ",") for x in split2]
    outcome = 0
    for i in split3:
        if len(i) == 2:
            try:
                multiply = int(i[0]) * int(i[1])
                outcome += multiply
            except:
                pass
    return outcome

input_test, input_real = aoc.getInputNotSplitted(current)

input = input_real
#input = input_test


outcome = part1(input)
print("The outcome of part one is: " + str(outcome))

splitted = split_string(input, "do()")
split2 = [split_string(x, "don't()")[0] for x in splitted]
sum_value = [part1(x) for x in split2]
print("The outcome of part one is: " + str(sum(sum_value)))