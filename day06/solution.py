#https://adventofcode.com/2023/day/4
import re

with open("test") as f:
    data = f.read().strip().splitlines()

# Part 1
def count_ways_to_win(time, record):
    cnt = 0
    for t in range(1,time):
        if t * (time-t) > record:
            cnt+=1
            print(t, "YES")
    return cnt


def p1results(data):
    times, records = re.findall(r'\d+', data[0]), re.findall(r'\d+', data[1])
    prod = 1
    for i in range(len(times)):
        prod = prod * count_ways_to_win(int(times[i]),int(records[i]))
    return prod

print("P1 RESULT: ", p1results(data))


# Part 2

def p2results(data):
    time, record = ''.join(re.findall(r'\d+', data[0])), ''.join(re.findall(r'\d+', data[1]))
    result = count_ways_to_win(int(time),int(record))
    return result

print("P2 RESULT: ", p2results(data))