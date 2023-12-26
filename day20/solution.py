#https://adventofcode.com/2023/day/20

import math

with open("input") as f:
    data = f.read().strip().splitlines()

modules, conjunctions = dict(), dict()
for l in data:
    name, dest = l.split(' -> ')
    # name: [module type, destination, state (False=low,True=high)]
    if name == 'broadcaster':
        modules[name] = ['*', dest.split(', '), False]
        continue
    if name[0] == '&':
        conjunctions[name[1:]] = dict()
    modules[name[1:]] = [name[0], dest.split(', '), False]
#print(modules)

for n,m in modules.items():
    for d in m[1]:
        if d in conjunctions.keys():
            conjunctions[d][n] = False
conjunctions_p2 = conjunctions.copy() # need this for part 2

# Part 1
def flip_flop(signal, state):
    if signal:
        return state
    return not state

def conjunct(name, signal, sender):
    conjunctions[name][sender] = signal
    for s in conjunctions[name].values():
        if not s:
            return True
    return False

def p1(mods, n=1000):
    low_count, high_count = 0, 0
    for i in range(n):
        q = [('broadcaster', False, 'button')] # queue of (destination, signal, sender)
        while q:
            curr = q.pop(0)
            name, s = curr[0], curr[1]
            #print(curr)
            #counting
            if s:
                high_count += 1
            else:
                low_count += 1

            try:
                t = mods[name][0]
            except:
                continue
            #handling signal
            if t == '%': # flip flop module
                if s: # if high signal to flip flop, next iteration
                    continue
                s = flip_flop(s, mods[name][2])
                mods[name][2] = s
            if t == '&': # conjunction module
                s = conjunct(name, s, curr[2])
                mods[name][2] = s
            # adding to queue
            for d in mods[name][1]:
                q.append((d, s, curr[0]))
    return high_count*low_count

print("P1 RESULT: ", p1(modules))

# Part 2

print("P2 RESULT: ", None)
