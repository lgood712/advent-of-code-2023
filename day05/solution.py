#https://adventofcode.com/2023/day/5
import re

with open("input") as f:
    data = f.read().strip()

# Part 1

def map_seeds(seeds, maps):
    min_location = float('inf')
    for x in map(int, seeds):
        for seg in maps:
            for conversion in re.findall(r'(\d+) (\d+) (\d+)', seg):
                destination, start, delta = map(int, conversion)
                if x in range(start, start + delta):
                    x += destination - start
                    break

        min_location = min(x, min_location)
    return min_location

def p1results(data):
    maps = data.split('\n\n')
    seeds = re.findall(r'\d+', maps[0])
    return map_seeds(seeds, maps[1:])

print("P1 RESULT: ", p1results(data))


# Part 2
def map_seed_ranges(segments):
    intervals = []

    for seed in re.findall(r'(\d+) (\d+)', segments[0]): # seeds
        x1, dx = map(int, seed)
        x2 = x1 + dx
        intervals.append((x1, x2, 1))

    min_location = float('inf')
    while intervals:
        x1, x2, level = intervals.pop()
        if level == 8:
            min_location = min(x1, min_location)
            continue

        for conversion in re.findall(r'(\d+) (\d+) (\d+)', segments[level]): # maps
            z, y1, dy = map(int, conversion)
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:    # no overlap
                continue
            if x1 < y1:                 # split original interval at y1
                intervals.append((x1, y1, level))
                x1 = y1
            if y2 < x2:                 # split original interval at y2
                intervals.append((y2, x2, level))
                x2 = y2
            intervals.append((x1 + diff, x2 + diff, level + 1)) # perfect overlap -> make conversion and let pass to next nevel 
            break

        else:
            intervals.append((x1, x2, level + 1))

    return min_location

def p2results(data):
    segments= data.split('\n\n')
    return map_seed_ranges(segments)

print("P2 RESULT: ", p2results(data))