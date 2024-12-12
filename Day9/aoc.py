import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import importAoC as aoc

input_test, input_real = aoc.getInput(current)

input = input_real
#input = input_test

input = input[0][0]

id = 0
f = True

def generate_output_str(input):
    f = True
    id = 0
    output = ""
    for c in input:
        c = int(c)
        i = 0
        if f:
            while i < c:
                output += str(id)
                i += 1
            id += 1
        else:
            while i < c:
                output += "."
                i+= 1
        f = not f
    return output

def put_in_order_blocks(s):
    s = [int(x) for x in s]
    files = s[::2]
    free = s[1::2]
    r_id = len(files) - 1
    l_id = 1
    # Start with the first data points
    data = [0 for x in range(files.pop(0))]
    fill = []
    while files:
        free_space = free.pop(0)
        for x in range(free_space):
            if not fill:
                fill = [r_id for y in range(files.pop())]
                r_id -= 1
            data.append(fill.pop(0))
        if files:
            data += [l_id for z in range(files.pop(0))]
            l_id += 1
    data += fill
    return data

def put_in_order_files(s):
    s = [int(x) for x in s]
    files = s[::2]
    free = s[1::2]
    f_id = len(files) - 1
    l_id = len(files) - 1
    #print(files, free)
    i = 0
    files_list = []
    files_info = []
    free_list = []
    free_info = []
    ff = 0
    for f in files:
        files_list.append([i for _ in range(f)])  
        files_info.append((ff,i,f))
        if free:
            free_size = free.pop(0)
            free_list.append(["." for _ in range(free_size)])
            free_info.append((ff+f, free_size))
            ff += free_size + f
        i += 1
    merged_list = []
    while files_list:
        merged_list += files_list.pop(0)
        if free_list:
            merged_list += free_list.pop(0)
    while files_info:
        file_start, f_id, file_size = files_info.pop()
        # find the first spot with enough room
        i = 0
        while i < len(free_info): # check, from left to right if there's enough room
            free_start, free_size = free_info[i]
            if file_size <= free_size and free_start < file_start: # enough room
                for j in range(file_size):
                    merged_list[free_start + j] = f_id
                    merged_list[file_start + j] = "."
                # When the filesize is equal to the free size, remove the free spot
                if file_size == free_size:
                    free_info.pop(i)
                else:
                    free_start = free_start + file_size
                    free_size = free_size - file_size
                    free_info[i] = (free_start, free_size)
                break
            i += 1
    return (merged_list)



def checksum(s):
    i = 0
    outcome = 0
    while i < len(s):
        if (s[i] != "."):
            outcome += i * int(s[i])
        i += 1
    return outcome

def partone(input):
    s = put_in_order_blocks(input)
    c = checksum(s)
    print(c)

def parttwo(input):
    s = put_in_order_files(input)
    c = checksum(s)
    print (c)

partone(input)
parttwo(input)
    