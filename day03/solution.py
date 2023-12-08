#https://adventofcode.com/2023/day/3

with open("input") as f:
    data = f.read().strip()

def is_symbol(chr):
    return not (chr.isdigit() or chr == '.') 

def find_number_coords(ls, row, col):
    r_check,c_check = [0],[0]
    if row != 0: r_check.append(-1)
    if row != len(ls)-1: r_check.append(1)
    if col != 0: c_check.append(-1)
    if row != len(ls[0])-1: c_check.append(1)
    coords = set((row+r,col+c) if ls[row+r][col+c].isdigit() else None for r in r_check for c in c_check)
    coords.discard(None)
    return coords

def extract_num(ls, row, col):
    num, coords, row_len = ls[row][col], [(row,col)], len(ls[row])
    # looking forwards
    val, f_col = ls[row][col+1], col+1
    while val.isdigit() :
        num = num + val
        coords.append((row,f_col))
        f_col=f_col+1
        if f_col >= row_len:
            break
        val =  ls[row][f_col]

    # looking backwards
    val, b_col = ls[row][col-1], col-1
    while val.isdigit():
        num =  val + num
        coords.append((row,b_col))
        b_col=b_col-1
        if b_col == -1:
            break
        val =  ls[row][b_col]
    #print("HELLO:", num, set(coords))
    return int(num), set(coords)


def parse_and_sum(data):
    ls = data.split("\n")
    row_len = len(ls[0])
    part_num_coords = set()
    for r in range(len(ls)):
        for c in range(row_len):
            if is_symbol(ls[r][c]):
                part_num_coords = part_num_coords.union(find_number_coords(ls, r, c))
    sum = 0
    accounted_for = set()
    for p in part_num_coords:
        #print("Coordinate:", p, ", Digit:", ls[p[0]][p[1]])
        if p not in accounted_for:
            num, coords = extract_num(ls, p[0], p[1])
            accounted_for = accounted_for.union(coords)
            sum = sum + num
    return sum


# Part 1
print("P1 RESULT: ", parse_and_sum(data))

# Part 2

def parse_gears_and_sum(data):
    ls = data.split("\n")
    row_len = len(ls[0])
    sum = 0
    for r in range(len(ls)):
        for c in range(row_len):
            if ls[r][c] == '*':
                num_coords = find_number_coords(ls, r, c)
                cnt, prod, accounted_for = 0, 1, set()
                for p in num_coords:
                    if p not in accounted_for:
                        num, coords = extract_num(ls, p[0], p[1])
                        accounted_for = accounted_for.union(coords)
                        prod = prod*num
                        cnt = cnt+1
                        if cnt > 2: break
                if cnt == 2:
                    sum = sum+prod
    return sum



print("P2 RESULT: ", parse_gears_and_sum(data))