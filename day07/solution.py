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
    top = hand[0]
    if top == 1:
        return 0 # high card
    if top == 2:
        if hand[1] == 2:
            return 2 # two pair
        return 1 # one pair
    if top == 3:
        if hand[1] == 2:
            return 4 # full house
        return 3 # three of a kind
    return top+1 # four or five of a kind

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
cards_p2 = 'J23456789TQKA'

def identify_class_p2(hand):
    jacks = hand.count('J')
    if jacks == 0:
        return identify_class(hand)
    if jacks == 5:
        return 6
    hand = sorted(Counter(hand.replace('J','')).values(), reverse=True)
    top = hand[0]

    if jacks + top == 2:
        return 1 # one pair
    if jacks + top == 3:
        if hand[1] == 2:
            return 4 # full house
        return 3 # three of a kind
    return jacks+top+1

def compare_hands_p2(hand1, hand2):
    class1 = identify_class_p2(hand1[0])
    class2 = identify_class_p2(hand2[0])
    if class1 > class2:
        return 1
    if class1 < class2:
        return -1
    for c1,c2 in zip(hand1[0], hand2[0]):
        if c1 == c2:
            continue
        return 1 if cards_p2.index(c1) > cards_p2.index(c2) else -1
    return 0    

def p2results(data):
    hands.sort(key=cmp_to_key(compare_hands_p2))
    total = 0
    for i in range(len(hands)):
        total += (i+1)*int(hands[i][1])
    return total

print("P2 RESULT: ", p2results(data))