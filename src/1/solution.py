#advent code challenge day 1 problem 1

import sys
s = set()
with open(sys.argv[1], 'r') as f:
    for line in f:
        l = int(line)
        if l in s: 
            print(l*(2020-l))
            sys.exit()
        else:
            s.add(2020-l)