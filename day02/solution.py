#https://adventofcode.com/2023/day/2
import re

with open("input") as f:
    data = f.read().strip()

def parse_and_sum(data):
    ls = data.split("\n")
    sum = 0
    for x in ls:
        red_max, green_max, blue_max =  max([int(r) for r in re.findall(r'(\d+)(?= red)', x)]), max([int(g) for g in re.findall(r'(\d+)(?= green)', x)]), max([int(b) for b in re.findall(r'(\d+)(?= blue)', x)])
        if red_max <= 12 and green_max <= 13 and blue_max <= 14:
            sum = sum + int(x[5:x.index(':')])
    return sum


# Part 1
print("P1 RESULT: ", parse_and_sum(data))

# Part 2
def parse_power_and_sum(data):
    ls = data.split("\n")
    sum = 0
    for x in ls:
        red_max, green_max, blue_max =  max([int(r) for r in re.findall(r'(\d+)(?= red)', x)]), max([int(g) for g in re.findall(r'(\d+)(?= green)', x)]), max([int(b) for b in re.findall(r'(\d+)(?= blue)', x)])
        sum = sum + red_max*green_max*blue_max
    return sum

print("P2 RESULT: ", parse_power_and_sum(data))