#https://adventofcode.com/2023/day/13
import numpy as np

with open("input") as f:
    data = f.read().strip().split('\n\n')

# Part 1 

def find_mirror_row(grid):
        n_rows = grid.shape[0]
        for r in range(1, n_rows):
            span = min(r, n_rows-r) # find max available # rows for mirror from this line
            top = grid[r-span : r][::-1] # above line, reversed for comp
            bottom = grid[r : r+span] # below line
            if np.array_equal(top, bottom):
                return r
        return None

def find_mirror_col(grid):
        n_cols = grid.shape[1]
        for c in range(1, n_cols):
            span = min(c, n_cols-c) # find max available # cols for mirror from this line
            left = grid[:, c-span : c][:, ::-1] # left of line, reversed for comp
            right = grid[:, c : c+span] # right of line
            if np.array_equal(left, right):
                return c
        return None
            
def p1results(data):
    total = 0
    for grid in data:
        grid = np.array([list(row) for row in grid.splitlines()])
        row_mirror = find_mirror_row(grid)
        if row_mirror is not None:
             total += row_mirror*100
        else:
             total += find_mirror_col(grid)
    return total
    

print("P1 RESULT: ", p1results(data))


# Part 2
def p2results(data):
    return

print("P2 RESULT: ", p2results(data))