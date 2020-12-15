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

'''
import sys

def conv(l):
    for i in range(len(l)):
        l[i] = set(l[i])
    return l

with open(sys.argv[1]) as f:
    read_data = f.read()

responses = [entry.split("\n") for entry in read_data.split("\n\n")]
count = 0

for entry in responses:
    count += len(set.intersection(*l))
print(count)
'''