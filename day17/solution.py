#https://adventofcode.com/2023/day/17

from collections import defaultdict
from itertools import count
from math import inf
from heapq import heappop, heappush


with open("input") as f:
    data = f.read().strip().splitlines()

grid = {i + 1j * j: int(x) for i, l in enumerate(data) for j, x in enumerate(l)}
l, w = len(data), len(data[0])
# Part 1 
def best_path(grid, l, w, p2=False):
    queue = [(0, 0, 0, 0, 0)]
    best = defaultdict(lambda: inf)
    c = count()
    while queue:
        dist, _, z, last_dir, dir_count = heappop(queue)

        if z == l - 1 + 1j * (w - 1) and (not p2 or dir_count > 3):
            return dist
        for dir in (1, -1, 1j, -1j):
            if dir == -last_dir or (p2 and last_dir and dir != last_dir and dir_count < 4):
                continue
            if dir == last_dir:
                new_dir_count = dir_count + 1
                if (not p2 and new_dir_count > 3) or (p2 and new_dir_count > 10):
                    continue
            else:
                new_dir_count = 1
            x = z + dir
            if x in grid:
                new_dist = dist + grid[x]
                if new_dist >= best[x, dir, new_dir_count]:
                    continue
                best[x, dir, new_dir_count] = new_dist
                heappush(queue, (new_dist, next(c), x, dir, new_dir_count))

print("P1 RESULT: ", best_path(grid,l,w))

# Part 2
print("P2 RESULT: ", best_path(grid,l,w,p2=True))