#https://adventofcode.com/2023/day/15

with open("input") as f:
    data = f.read().strip().split(',')


# Part 1 
    
def hash(s):
    current_val = 0
    for c in s:
        current_val = ( (current_val + ord(c)) *17) % 256
    return current_val

total = 0
for s in data:
    total+= hash(s)        

print("P1 RESULT: ", total)

# Part 2
# dictionary: {box#: {label: focal}}
boxes = dict()
for s in data:
    if '=' in s: # run box step (addition/replacement)
        label, foc = s.split('=')
        box_num = hash(label)
        boxes[box_num] = boxes.get(box_num, {label: int(foc)})
        boxes[box_num][label] = int(foc)
    else:
        # run box step (removal)
        label = s.replace('-', '')
        box_num = hash(label)
        if box_num in boxes:
            boxes[box_num].pop(label, None)

total = 0
for b, d in boxes.items():
    for i, v in enumerate(d.values()):
        total += (b+1) * (i+1) * v

print("P2 RESULT: ", total)