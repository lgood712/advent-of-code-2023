#https://adventofcode.com/2023/day/21

with open("input") as f:
    data = f.read().strip().splitlines()

grid = {i + 1j * j: x for i, l in enumerate(data) for j, x in enumerate(l)}
rocks, plots = set(), set()
for loc, val in grid.items():
    if val == ".":
        plots.add(loc)
    elif val == '#':
        rocks.add(loc)
    else: # S
        plots.add(loc)
        start = loc

dirs = (1, -1, 1j, -1j)

# Part 1


def evaluate_steps(start, n):
    possible_dests = set()
    #print(start,n)
    # base
    if n == 0:
        return set([start])
    
    for d in dirs:
        step = start + d
        if step in plots:
            possible_dests.update(evaluate_steps(step, n-1))
    
    return possible_dests


print("P1 RESULT: ", len(evaluate_steps(start, 64)))

# Part 2



print("P2 RESULT: ", None)
