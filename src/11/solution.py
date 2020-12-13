import sys
import string

with open(sys.argv[1]) as f:
    groups = f.read().split('\n\n')

count = 0
for group in groups:
    questions = {c for c in group if c in string.ascii_lowercase}
    count += len(questions)

print(count)

'''
import sys

with open(sys.argv[1]) as f:
    read_data = f.read()

responses = [entry.replace("\n", "") for entry in read_data.split("\n\n")]
count = 0
for entry in responses:
    count += len(set(entry))

print(count)
'''