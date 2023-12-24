#https://adventofcode.com/2023/day/19

import numpy as np

with open("input") as f:
    wf, parts = [l.splitlines() for l in f.read().strip().split("\n\n")]

workflows = dict()
for w in wf:
    name, workflow = w.replace('}','').split("{")
    workflows[name] = [s.split(":") for s in workflow.split(",")]


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


print("P2 RESULT: ", None)
