#advent code day 3 problem 2

import sys
import re

SLOPE_Y = int(sys.argv[2])
SLOPE_X = int(sys.argv[3])

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