#https://adventofcode.com/2023/day/11

import re

with open("input") as f:
    data = f.read().strip().splitlines()

# Part 1 
def find_galaxies_and_multipliers(data, x_factor = 2):
    galaxies, row_multipliers, col_multipliers = [], [1]*len(data), [1]*len(data[1])
    empty_cols = set(range(len(data[0])))
    # iterate over rows
    for i, r in enumerate(data):
        gals = set(j for j, c in enumerate(r) if c == '#') # check for galaxy in row
        if len(gals) == 0 :
            row_multipliers[i] = x_factor # add expansion multiplier if no galaxies in row
        for g in gals:
            galaxies.append((i,g)) # record galaxy coordinates
        empty_cols = empty_cols - gals # keep track of empty columns for column multipliers later
    # iterate over recorded empty columns and add expansion multipliers where needed
    for c in empty_cols:
        col_multipliers[c] = x_factor
    return galaxies, row_multipliers, col_multipliers

def sum_path_lens(galaxies, row_multipliers, col_multipliers):
    # identify distance between each pair
    sum = 0
    for i in range(len(galaxies)-1):
        g1 = galaxies[i]
        for g2 in galaxies[i+1:]:
            start, end = g1[0], g2[0]
            if start > end:
                start,end = end, start
            for r in row_multipliers[start:end]:
                sum += 1*r 
            start, end = g1[1], g2[1]
            if start > end:
                start,end = end, start
            for c in col_multipliers[start:end]:
                sum += 1*c 
    return sum


def p1results(data):
    galaxies, row_multipliers, col_multiplers = find_galaxies_and_multipliers(data, 2)
    return sum_path_lens(galaxies, row_multipliers, col_multiplers)

print("P1 RESULT: ", p1results(data))


# Part 2
def p2results(data):
    galaxies, row_multipliers, col_multiplers = find_galaxies_and_multipliers(data, 1000000)
    return sum_path_lens(galaxies, row_multipliers, col_multiplers)

print("P2 RESULT: ", p2results(data))