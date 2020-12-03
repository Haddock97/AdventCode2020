# advent code challenge day 2 problem 1
import sys
import re

valid_passwords_count = 0

with open(sys.argv[1]) as f:
    for line in f:
        matches = re.fullmatch(r'(\d+)\-(\d+) ([a-z]): ([a-z]+)\n?', line)
        min_count = int(matches.group(1))
        max_count = int(matches.group(2))
        [letter, password] = matches.group(3, 4)
        letter_count = password.count(letter)

        if min_count <= letter_count <= max_count:
            valid_passwords_count += 1

print(valid_passwords_count)

"""
# advent code challenge day 2 problem 1
import sys

counter = 0
result = 0

with open(sys.argv[1]) as f:
    for line in f:
        parts = line.split()
        numbers = parts[0].split("-")
        c_min = int(numbers[0])
        c_max = int(numbers[1])
        letter = parts[1][0]
        password = parts[2]

        letter_count = password.count(letter)

        if c_min <= letter_count <= c_max:
            result += 1

    print(result)
    """
