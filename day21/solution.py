#https://adventofcode.com/2023/day/21
from collections import deque

with open("input") as f:
    data = f.read().strip().splitlines()

grid = {i + 1j * j: x for i, l in enumerate(data) for j, x in enumerate(l)}
plots = set()
for loc, val in grid.items():
    if val == '.':
        plots.add(loc)
    elif val == 'S':
        plots.add(loc)
        start = loc

# Part 1


def evaluate_steps(start, steps):
    visited, q = set(), deque([(start,0)])
    even_cnt, odd_cnt = 0,0
    #print(start,n)
    while True:
        try:
            loc = q.popleft()
        except:
            return odd_cnt if steps % 2 else even_cnt
        
        n, loc = loc[1], loc[0]
        if n > steps:
            continue

        for d in (1, -1, 1j, -1j):
            step = loc+d
            if step in visited or not step in plots:
                # there's something i need to do here
                continue
            
            q.append((step, n+1))
            visited.add(step)
            print(step,n)
            if n % 2:
                even_cnt += 1
            else:
                odd_cnt += 1


print("P1 RESULT: ", evaluate_steps(start, 64))

# Part 2



print("P2 RESULT: ", None)
