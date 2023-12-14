#https://adventofcode.com/2023/day/7
import re
from collections import Counter
from functools import cmp_to_key

with open("input") as f:
    data = f.read().strip().splitlines()

hands = [tuple(l.split(' ')) for l in data]
cards = '23456789TJQKA'

# Part 1
def identify_class(hand):
    hand = sorted(Counter(hand).values(), reverse=True)
    if hand[0] == 1:
        return 0 # high card
    if hand[0] == 2:
        if hand[1] == 2:
            return 2 # two pair
        return 1 # one pair
    if hand[0] == 3:
        if hand[1] == 2:
            return 4 # full house
        return 3 # three of a kind
    return hand[0]+1 # four or five of a kind

def compare_hands(hand1, hand2):
    class1 = identify_class(hand1[0])
    class2 = identify_class(hand2[0])
    if class1 > class2:
        return 1
    if class1 < class2:
        return -1
    for c1,c2 in zip(hand1[0], hand2[0]):
        if c1 == c2:
            continue
        return 1 if cards.index(c1) > cards.index(c2) else -1
    return 0

def p1results(hands):
    hands.sort(key=cmp_to_key(compare_hands))
    total = 0
    for i in range(len(hands)):
        total += (i+1)*int(hands[i][1])
    return total

print("P1 RESULT: ", p1results(hands))


# Part 2

def p2results(data):
    return

print("P2 RESULT: ", p2results(data))