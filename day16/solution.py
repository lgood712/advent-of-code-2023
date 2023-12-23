#https://adventofcode.com/2023/day/16

import sys
sys.setrecursionlimit(10**6)

with open("input") as f:
    data = f.read().strip().splitlines()

grid = {i + 1j * j: x for i, l in enumerate(data) for j, x in enumerate(l)}

# Part 1 
# directions will be 1 (down), -1 (up), 1j (right), -1j (left)
def step(grid, loc, dir, l, w, visited=set()):
    # base case: hitting a wall or repeating a loc + dir combo
    if loc.real < 0 or l - loc.real <= 0 or loc.imag < 0 or w - loc.imag <= 0 or (loc,dir) in visited:
        #print('base')
        return visited
    # add location to visited tracking
    visited.add((loc,dir))
    # conditions
    space = grid[loc]
    if space == '.' or (space == '-' and dir in (1j,-1j)) or (space == '|' and dir in (1,-1)): # continue on path
        #print('straight')
        return step(grid, loc+dir, dir, l, w, visited)
    elif space == '-':
        #print('h-split')
        return step(grid, loc+1j, 1j, l, w, visited).union(step(grid, loc-1j, -1j, l, w, visited))
    elif space == '|':
        #print('v-split')
        return step(grid, loc+1, 1, l, w, visited).union(step(grid, loc-1, -1, l, w, visited))
    elif dir == -1:
        if space == '\\':
            #print('up-left')
            return step(grid, loc-1j, -1j, l, w, visited)
        if space == '/':
            #print('up-right')
            return step(grid, loc+1j, 1j, l, w, visited)
    elif dir == 1:
        if space == '\\':
            #print('down-right')
            return step(grid, loc+1j, 1j, l, w, visited)
        if space == '/':
            #print('down-left')
            return step(grid, loc-1j, -1j, l, w, visited)
    elif dir == 1j:
        if space == '\\':
            #print('right-down')
            return step(grid, loc+1, 1, l, w, visited)
        if space == '/':
            #print('right-up')
            return step(grid, loc-1, -1, l, w, visited)
    else: # dir == -1j
        if space == '\\':
            #print('left-up')
            return step(grid, loc-1, -1, l, w, visited)
        if space == '/':
            #print('left-down')
            return step(grid, loc+1, 1, l, w, visited)

l,w = len(data), len(data[0])
tile_dir = step(grid, 0j, 1j, l, w)
tiles = set([t[0] for t in tile_dir])
print("P1 RESULT: ", len(tiles))

# Part 2
max_energized = 0
# check all rows on either side
for x in range(l):
    v = set([t[0] for t in step(grid,x+0j,1j, l, w, set())])
    max_energized = max(len(v),max_energized)
    v = set([t[0] for t in step(grid,x+((l-1)*1j),-1j, l, w, set())])
    max_energized = max(len(v),max_energized)

# check all columns on top and bottom
for y in range(w):
    v = set([t[0] for t in step(grid,(y*1j), 1, l, w, set())])
    max_energized = max(len(v),max_energized)
    v = set([t[0] for t in step(grid,(w-1)+(y*1j),-1, l, w, set())])
    max_energized = max(len(v),max_energized)

print("P2 RESULT: ", max_energized)