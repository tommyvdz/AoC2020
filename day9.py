from sys import argv
import sys
from copy import deepcopy

def main():
    if len(argv) != 3:
        print("Usage: python program.py input.txt preamble")
        sys.exit(1)
    elif ".txt" not in argv[1]:
        print("Input must be a txt file")
        sys.exit(1)

    stream = []

    with open(argv[1]) as f:
        input = f.readlines()
        stream = [int(x) for x in input]
    
    preamble = int(argv[2]) 
    
    valid = True
    i = preamble+1
    while valid:
        number = stream[i-1]
        valid = checkPreamble(number, stream[(i-preamble-1):i-1])
        i += 1
    print(f'Answer 1 is {number}')
    answer = []
    while sum(answer) != number:
        answer = findSet(number,stream)
        stream = stream[1:]
    print(f'Answer 2 is {min(answer)+max(answer)}')
    
def checkPreamble(number, preamble):
    a = 0
    b = 0
    for a in preamble:
        b = number - a
        if b in preamble:
            return True
    return False

def findSet(number, stream):
    numberset = []
    total = 0
    i = 0
    while total < number and i < len(stream):
        numberset.append(stream[i])
        total = sum(numberset)
        i += 1
    return numberset

main()
