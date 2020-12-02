#advent code challenge day 1 problem 1

import sys
s = {}
with open(sys.argv[1], 'r') as f:
    for line in f:
        l = int(line)
        if (2020 - l) in s: 
            print(l*(2020-l))
            break
        else:
            s.add(2020-l)