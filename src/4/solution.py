# advent code challenge day 2 problem 1
import sys
import re

valid_passwords_count = 0

with open(sys.argv[1]) as f:
    for line in f:
        matches = re.fullmatch(r'(\d+)\-(\d+) ([a-z]): ([a-z]+)\n?', line)
        min_index = int(matches.group(1)) - 1
        max_index = int(matches.group(2)) - 1
        [letter, password] = matches.group(3, 4)
        if (password[min_index] == letter) != (password[max_index] == letter):
            valid_passwords_count += 1

print(valid_passwords_count)