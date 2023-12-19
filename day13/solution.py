#https://adventofcode.com/2023/day/13
import numpy as np

with open("input") as f:
    data = f.read().strip().split('\n\n')


def find_mirror(a, smudge=0):
    for i in range(1, len(a)):
        n = min(i, len(a) - i)
        if np.sum(a[:i][::-1][:n] ^ a[i:][:n]) == smudge:
            return i


# Part 1 
            
def p1results(data):
    total = 0
    for grid in data:
        a = np.array([[x == "#" for x in l] for l in grid.split()])
        total += (
            100 * row
            if (row := find_mirror(a))
            else find_mirror(a.T)
        )
    return total
    

print("P1 RESULT: ", p1results(data))


# Part 2
def p2results(data):
    total = 0
    for grid in data:
        a = np.array([[x == "#" for x in l] for l in grid.split()])
        total += (
            100 * row
            if (row := find_mirror(a, 1))
            else find_mirror(a.T, 1)
        )
    return total

print("P2 RESULT: ", p2results(data))