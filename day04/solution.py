#https://adventofcode.com/2023/day/4
import re

with open("input") as f:
    data = f.read().strip()

def parse_and_sum(data):
    ls = data.splitlines()
    sum = 0
    for l in ls:
        win, my_nums = l[l.index(': ')+2:].split(' | ')
        win, my_nums = set(re.split('  | ', win.strip())), set(re.split('  | ', my_nums.strip()))
        matches = len(win.intersection(my_nums))
        if matches > 0:
            sum = sum + 1*2**(matches-1)
        
    return sum


# Part 1
print("P1 RESULT: ", parse_and_sum(data))

# Part 2

def count_cards(game_results, card_number):
    num_matches = game_results[card_number]
    # base case: card that does not win
    if num_matches == 0:
        return 1
    # otherwise run count_cards for the n next cards
    cnt = 1
    for g in range(card_number+1,card_number+num_matches+1):
        cnt = cnt + count_cards(game_results, g)
    return cnt

def parse_and_count_matches(data):
    ls = data.splitlines()
    game_results = []
    for l in ls:
        win, my_nums = l[l.index(': '):].split(' | ')
        win, my_nums = set(re.split('  | ', win.strip())), set(re.split('  | ', my_nums.strip()))
        matches = len(win.intersection(my_nums))
        game_results.append(matches)
    return game_results

def p2results(data):
    game_results = parse_and_count_matches(data)
    cnt = 0
    for g in range(len(game_results)):
        cnt = cnt + count_cards(game_results, g)
    return cnt

print("P2 RESULT: ", p2results(data))