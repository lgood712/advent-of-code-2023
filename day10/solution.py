#https://adventofcode.com/2023/day/10

with open("input") as f:
    data = f.read().strip().splitlines()

# Part 1 
def find_s(data):
    for r in range(len(data)):
        c = data[r].find('S')
        if c != -1:
            return (r,c)
        
def step(data, loc, approach, pipe):
    r,c = loc[0], loc[1]
    if approach == (0,0):
        # check all directions and pick first viable if first step
        check = data[r-1][c]
        if check == '|' or check == '7' or check == 'F':
            return (r-1, c), (1,0), check
        check = data[r+1][c]
        if check == '|' or check == 'L' or check == 'J':
            return (r+1, c), (-1,0), check
        check = data[r][c-1]
        if check == '-' or check == 'F' or check == 'L':
            return (r, c-1), (0,1), check
        check = data[r][c+1]
        if check == '-' or check == '7' or check == 'J':
            return (r, c+1), (0,-1), check
    # else follow the pipe at current
    # vertical approach
    a = approach[0]
    if a != 0:
        if a == -1: # from above
            if pipe == '|':
                return (r+1, c), (-1,0), data[r+1][c]
            if pipe == 'L':
                return (r, c+1), (0,-1), data[r][c+1]
            if pipe == 'J':
                return (r, c-1), (0,1), data[r][c-1]
        # from below
        if pipe == '|':
            return (r-1, c), (1,0), data[r-1][c]
        if pipe == '7':
            return (r, c-1), (0,1), data[r][c-1]
        if pipe == 'F':
            return (r, c+1), (0,-1), data[r][c+1]
    # horizontal approach
    if approach[1] == -1: # from the left
        if pipe == '-':
            return (r, c+1), (0,-1), data[r][c+1]
        if pipe == '7':
            return (r+1, c), (-1,0), data[r+1][c]
        if pipe == 'J':
            return (r-1, c), (1,0), data[r-1][c]
    # from the right
    if pipe == '-':
        return (r, c-1), (0,1), data[r][c-1]
    if pipe == 'L':
        return (r-1, c), (1,0), data[r-1][c]
    if pipe == 'F':
        return (r+1, c), (-1,0), data[r+1][c]

    
def find_loop_len(data):
    start = find_s(data)
    step_cnt, approach = 1, (0,0)
    loc, approach, pipe = step(data, start, approach, '')
    while 0<1:
        print(loc, approach, pipe)
        if loc == start:
            return step_cnt
        loc, approach, pipe = step(data, loc, approach, pipe)
        step_cnt += 1
        


def p1results(data):
    return int(find_loop_len(data) / 2)

print("P1 RESULT: ", p1results(data))


# Part 2

def p2results(data):
    return

print("P2 RESULT: ", p2results(data))