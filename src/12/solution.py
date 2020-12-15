import sys

with open(sys.argv[1]) as f:
    groups = []
    for lines in f.read().split('\n\n'):
        group = []
        for line in lines.strip().split('\n'):
            group.append(set(line))
        groups.append(group)

count = 0
for group in groups:
    count += len(set.intersection(*group))

print(count)
