#https://adventofcode.com/2023/day/14

with open("input") as f:
    data = f.read().strip().splitlines()

grid = {i + 1j * j: x for i, l in enumerate(data) for j, x in enumerate(l)}
cubes = {loc for loc, val in grid.items() if val == "#"}
rounds = {loc for loc, val in grid.items() if val == "O"}


# Part 1 
def tilt(rounds, dir=1):
    while True:
        open = grid.keys() - rounds - cubes
        new_rounds = {s - dir if s - dir in open else s for s in rounds}
        if new_rounds == rounds:
            return new_rounds
        rounds = new_rounds

def calc_load(rounds):
    return sum(len(data) - r.real for r in rounds)

           
tilted_n = tilt(rounds)
print("P1 RESULT: ", calc_load(tilted_n))

# Part 2
def spin(rounds, cycles=1):
    record, c = [], 0
    while c < cycles:
        for dir in (1,1j,-1,-1j):
            rounds = tilt(rounds, dir)
        if rounds in record:
            start = record.index(rounds)
            return record[(cycles - c) % (start - c) + c - 1]
        record.append(rounds)
        c+=1
    return rounds

spun = spin(rounds, 1000000000)
print("P2 RESULT: ", calc_load(spun))