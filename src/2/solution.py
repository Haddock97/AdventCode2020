# advent code challenge day 1 problem 2
import sys
# input: set of numbers and target integer
# output: set of two ints from numbers that sum to target
def find_pair(numbers, target):
    for num in numbers:
        if target - num in numbers:
            return (target - num, num)

with open(sys.argv[1]) as f:
    # get list of ints
    numbers = {int(line) for line in f}
    for num in numbers:
        result = find_pair(numbers, 2020 - num)
        if result is not None:
            print(2020-num * result[0] * result[1])
            sys.exit()