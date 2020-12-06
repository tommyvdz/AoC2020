
from sys import argv
import math
import sys

def main():
    if len(argv) != 2:
        print("Usage: python program input.txt")
        sys.exit(1)
    elif ".txt" not in argv[1]:
        print("Input must be a txt file")
        sys.exit(1)

    bpasses = list()
    bpassids = dict()
    highest = 0
    with open(argv[1]) as f:
        bpasses = f.read().splitlines() 
    
    for bpass in bpasses:
        result = calculateID(row(bpass, 0, 127), column(bpass[len(bpass)-3:],0,7))
        bpassids[bpass] = result
        if result >= highest:
           highest = result
    
    for number in range(0,980):
        if number not in bpassids.values() and number+1 in bpassids.values() and number-1 in bpassids.values():
            print(number)
        


def row(bpass, low, high):
    c = bpass[0]
    bpass = bpass[1:]
    if len(bpass)==3: # base case
        if c == 'F':
            return low
        if c == 'B':
            return high
    if c == 'F':
        high = math.floor(high - ((high-low)/2))
    if c == 'B':
        low = math.ceil(low + ((high-low)/2))
    return row(bpass,low,high)

def column(bpass, low, high):
    c = bpass[0]
    if len(bpass)==1: # base case
        if c == 'R':
            return high
        if c == 'L':
            return low
    bpass = bpass[1:]
    if c == 'L':
        high = math.floor(high - ((high-low)/2))
    if c == 'R':
        low = math.ceil(low + ((high-low)/2))
    return column(bpass,low,high)

def calculateID(row, column):
    return (row * 8) + column

main()