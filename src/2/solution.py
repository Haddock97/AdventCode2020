# advent code challenge day 1 problem 2
import sys
# input: set of numbers and target integer
# output: set of two ints from numbers that sum to target
def find_pair(numbers, target):
    for each in numbers:
        if target - each in numbers:
            return {target - each, each}

with open(sys.argv[1]) as f:
    # get list of ints
    numbers = {int(line) for line in f}
    # print(numbers)

    for line in f:
        s = find_pair(numbers, 2020 - int(line))
        print(2020-int(line) * s[0] * s[1])
        sys.exit()