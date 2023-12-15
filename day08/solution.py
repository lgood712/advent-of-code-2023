#https://adventofcode.com/2023/day/8
import re
from collections import Counter
from functools import cmp_to_key

with open("input") as f:
    data = f.read().strip().split('\n\n')

directions = [0 if d == 'L' else 1 for d in data[0]]
ntwk = {}
for l in data[1].split('\n'):
    ind, tup = l.split(' = ')
    tup = re.findall(r'([A-Z0-9][A-Z0-9][A-Z0-9].*?)', tup)
    ntwk[ind] = (tup[0],tup[1])
#print(directions)
#print(ntwk)

# Part 1
def find_z(directions,ntwk):
    current = 'AAA'
    step_cnt = 0
    while current != 'ZZZ':
        for d in directions:
            if current == 'ZZZ':
                return step_cnt
            step_cnt += 1
            current = ntwk[current][d]
    return step_cnt


def p1results(directions, ntwk):
    return find_z(directions, ntwk)

print("P1 RESULT: ", p1results(directions, ntwk))


# Part 2

def find_ends_in_z(directions,ntwk):
    currents, nexts = [], []
    for k in ntwk.keys():
        if k[2] == 'A':
            currents.append(k)
    step_cnt, num_zs, target = 0, 0, len(currents)
    while num_zs < target:
        for d in directions:
            step_cnt += 1
            nexts, num_zs = [], 0
            for c in currents:
                new = ntwk[c][d]
                if new[2] == 'Z':
                    num_zs += 1
                    if num_zs == target:
                        return step_cnt
                nexts.append(new)
            currents = nexts
    return step_cnt


def p2results(directions, ntwk):
    return find_ends_in_z(directions, ntwk)

print("P2 RESULT: ", p2results(directions, ntwk))