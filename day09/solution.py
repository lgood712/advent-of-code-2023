#https://adventofcode.com/2023/day/8
import re
from collections import Counter
from functools import cmp_to_key

with open("input") as f:
    data = f.read().strip().splitlines()
data = [[int(n) for n in d.split()] for d in data]

# Part 1
def get_diffs(seq):
    current, next, diffs, zeroed = seq, [], [], False
    # reduce to zero diffs
    while not zeroed:
        zeroed = True
        for i in range(len(current) - 1):
            diff = current[i+1] - current[i]
            next.append(diff)
            if zeroed and diff != 0:
                zeroed = False
        diffs.append(next)
        current, next = next, []
    #print(diffs)
    return diffs
    
def extrapolate(seq, forward = True):
    diffs = get_diffs(seq)
    next = 0
    if not forward: 
        for d in diffs[::-1][1:]:
            next = d[0] - next
        return seq[0] - next
    else:
        for d in diffs[::-1][1:]:
            next = d[-1] + next
        return seq[-1] + next

def p1results(data):
    sum = 0
    for seq in data:
        sum += extrapolate(seq)
    return sum

print("P1 RESULT: ", p1results(data))


# Part 2

def p2results(directions, ntwk):
    sum = 0
    for seq in data:
        sum += extrapolate(seq, False)
    return sum

print("P2 RESULT: ", p2results(data, data))