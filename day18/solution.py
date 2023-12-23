#https://adventofcode.com/2023/day/18

import numpy as np

with open("input") as f:
    data = f.read().strip().splitlines()

plan = []
for l in data:
    d, n, hex = l.split(' ')
    if d == 'R':
        d = 1j
    elif d == 'L':
        d = -1j
    elif d == 'U':
        d = -1
    elif d == 'D':
        d = 1
    plan.append((d,int(n),hex[1:-1]))

# Part 1 
def dig_trench(plan):
    lengths = np.array([d * n for d, n, _ in plan])
    return abs(np.sum(np.cumsum(lengths.real) * lengths.imag)) + np.sum(np.abs(lengths)) / 2 + 1


print("P1 RESULT: ", dig_trench(plan))

# Part 2
new_plan = []
for _,_,hex in plan:
    new_d, new_n = int(hex[6]), int(hex[1:6],16)
    if new_d == 0:
        new_d = 1j
    elif new_d == 2:
        new_d = -1j
    elif new_d == 3:
        new_d = -1
    elif new_d == 1:
        new_d = 1
    new_plan.append((new_d,new_n,hex))

print("P2 RESULT: ", dig_trench(new_plan))
