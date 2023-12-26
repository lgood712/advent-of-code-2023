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
#conjunctions_p2 = conjunctions.copy() # need this for part 2

# Part 1
def flip_flop(signal, state):
    if signal:
        return state
    return not state



def p1(mods, cons, n=1000):

    def conjunct(name, signal, sender):
        cons[name][sender] = signal
        for s in cons[name].values():
            if not s:
                return True
        return False

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

print("P1 RESULT: ", p1(modules, conjunctions))

# Part 2
# Manual investigation:
# rx needs to receive a low pulse from &cs
# &cs sends a low pulse when it receives a high pulse from one of
# &kh, &lz, &tg, &hn
# and the other three last sent a high pulse to &cs

# Therefore, we need to find a patterned cycle for each of those 4 modules
# then identify when they would overlap.


print("P2 RESULT: ", None)
