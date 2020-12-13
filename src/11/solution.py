import sys
import string

with open(sys.argv[1]) as f:
    groups = f.read().split('\n\n')

count = 0
for group in groups:
    questions = {c for c in group if c in string.ascii_lowercase}
    count += len(questions)

print(count)
