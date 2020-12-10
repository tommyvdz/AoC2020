from sys import argv
import sys
import numpy as np
import app

def main():
    input = app.input()
    adapters = list()
    for line in input:
        adapters.append(int(line))
    adapters.append(0) #starting from the outlet which is rated 0
    adapters.append(max(adapters)+3) #the built-in adapter is always 3 higher than the highest adapter
    adapters = sorted(adapters)
    differences = solve1(adapters)
    possibilities = solve2(adapters)
    print(f'Answer 1 = {differences.count(1)*differences.count(3)} and Answer 2= {possibilities}')

def solve1(adapters: list):
    differences = []
    for i, a1 in enumerate(adapters):
        for a2 in adapters[i+1:]:
            if a2 - a1 <= 3:
                differences.append(a2-a1)
                break
    return differences

def solve2(adapters: list):
    # had to turn to reddit for help on part 2
    possibilities = {adapters[-1]: 1}
    for a in reversed(adapters[:-1]):
        possibilities[a] = sum(possibilities.get(x, 0) for x in (a+1, a+2, a+3))
    return possibilities[0]

main()
