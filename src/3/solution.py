# advent code challenge day 2 problem 1
import sys
import re

"""
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
ANSWER: 2
"""

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
