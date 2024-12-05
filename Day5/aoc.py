import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc

input_test, input_real = aoc.getInput(current)

input = input_real
#input = input_test

empty_row = [len(x) for x in input].index(0)
rules = [list(map(int, (x[0].split("|")))) for x in input[0:empty_row]]
rules_first = [int(x[0]) for x in rules]
rules_second = [int(x[1]) for x in rules]
order = input[empty_row+1:]

def get_middle(input_list):
    middle = float(len(input_list)) / 2
    if middle % 2 != 0:
        return input_list[int(middle - 0.5)]
    else:
        return (input_list[int(middle - 0.5)], input_list[int(middle + 0.5)])

def get_correct_pages(all_pages):
    i = 0
    while i < len(all_pages):
        pages_done = all_pages[:i]
        current_page = int(all_pages[i])
        # Get the pages for the pages which needs to be printed before the active one
        idx_before = [x for x in range(len(rules_second)) if rules_second[x] == current_page]
        must_be_printed_before = [rules_first[x] for x in idx_before]
        for page_done in pages_done:
            if page_done not in must_be_printed_before:
                return False
        i += 1
    return all_pages

def reorder_pages(all_pages):
    i = 0
    while i < len(all_pages):
        changed = False
        pages_done = all_pages[:i]
        pages_to_do = all_pages[i+1:]
        current_page = int(all_pages[i])
        # Get the pages for the pages which needs to be printed before the active one
        rules_before = sorted([rules[x][0] for x in range(len(rules_second)) if rules_second[x] == current_page])
        rules_after = sorted([rules[x][1] for x in range(len(rules_first)) if rules_first[x] == current_page])
        # check pages to the right
        for page_to_do in pages_to_do:
            # if the page is to the right, but should be to the left
            if page_to_do in rules_before:
                idx_to_move = all_pages.index(page_to_do)
                el = all_pages.pop(idx_to_move)
                idx_to_pos = all_pages.index(current_page)
                all_pages.insert(idx_to_pos, el)
                changed = True
                break
        # check pages to the left
        for page_done in pages_done[::-1]:
            # if the page is to the left, but should be on the right
            if page_done in rules_after:
                idx_to_move = all_pages.index(page_done)
                el = all_pages.pop(idx_to_move)
                idx_to_pos = all_pages.index(current_page)
                all_pages.insert(idx_to_pos, el)
                changed = True
                break
        if not changed:
            i+= 1
    return all_pages

correct_order = []
for row in order:
    row = [int(x) for x in row]
    correct = get_correct_pages(row)
    if correct:
        correct_order.append(correct)

pt1 = 0
for c in correct_order:
    m = get_middle(c)
    pt1 += m
print ("The outcome of part one is: " + str(pt1))

# Change all values to ints
order = [[int(y) for y in x] for x in order]

# Remove the correct_orders
for x in correct_order:
    if x in order:
        order.remove(x)

reordered = []
for row in order:
    row = [int(x) for x in row]
    incorrect = reorder_pages(row)
    if incorrect:
        reordered.append(incorrect)

pt2 = 0
for c in reordered:
    m = get_middle(c)
    pt2 += m
print ("The outcome of part two is: " + str(pt2))