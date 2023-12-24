#https://adventofcode.com/2023/day/19

import math

with open("input") as f:
    wf, parts = [l.splitlines() for l in f.read().strip().split("\n\n")]

workflows = dict()
for w in wf:
    name, workflow = w.replace('}','').split("{")
    workflows[name] = [tuple(s.split(":")) for s in workflow.split(",")]

def process_part(part):
    part = [int(x[1]) for x in [a.split("=") for a in part[1:-1].split(",")]]
    x,m,a,s = part[0],part[1], part[2], part[3]
    curr = 'in'
    while True:
        for w in workflows[curr]:
            stmt = w[0]
            if len(w) == 1:
                if stmt == 'A':
                    return x+m+a+s
                if stmt == 'R':
                    return 0
                curr = stmt
                break
            if eval(stmt):
                curr = w[1]
                if curr == 'A':
                    return x+m+a+s
                if curr == 'R':
                    return 0
                break


# Part 1 
total = 0
for p in parts:
    total += process_part(p)
    


print("P1 RESULT: ", total)

# Part 2

start = ('in', (1, 4000), (1, 4000), (1, 4000), (1, 4000))
q = [start]
accepted = 0

while q:
    curr, *intervals = q.pop()
    if type(curr) == tuple:
        curr = curr[0]
    if curr in ('A', 'R'):
        if curr == 'A':
            accepted += math.prod(high-lo+1 for lo, high in intervals)
        continue
    for cond, outcome in workflows[curr][:-1]:
        idx, operator, amt = cond[0], cond[1], int(cond[2:])
        idx = 'xmas'.index(idx)
        low, high = intervals[idx]

        if (operator == '>' and amt >= high) or (operator == '<' and amt <= low):
            continue

        if (operator == '>' and amt < low) or (operator == '<' and amt > high):
            q.append((outcome, *intervals))
            break

        if operator == '>':
            transfer = (amt+1, high)
            passthrough = (low, amt)
        else:
            transfer = (low, amt-1)
            passthrough = (amt, high)
        intervals[idx] = passthrough
        intervals2 = intervals.copy()
        intervals2[idx] = transfer
        q.append((outcome, *intervals2))

    else:
        q.append((workflows[curr][-1], *intervals))


print("P2 RESULT: ", accepted)
