#advent code challenge day 3 problem 1
'''
import sys

with open(sys.argv[1]) as f:
    my_map = [line.rstrip() for line in f]

    height = len(my_map) - 1
    width = len(my_map[0])
    trees = 0
    x = 0
    y = 0

    for _i in range(height):
        y += 1
        x = (x + 3) % width
        #print(f'x: {x} y: {y}')
        if my_map[y][x] == "#":
            trees += 1
    print(trees)
'''
#advent code challenge day 3 problem 1

import sys
import re

SLOPE_Y = 1
SLOPE_X = 3

with open(sys.argv[1]) as f:
    my_map = [line.rstrip() for line in f]

width = len(my_map[0])
x = 0
y = 0
trees_count = 0

while y < len(my_map):
    if my_map[y][x % width] == '#':
        trees_count += 1

    y += SLOPE_Y
    x += SLOPE_X

print(trees_count)
