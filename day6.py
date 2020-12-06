from sys import argv
import sys

def main():
    if len(argv) != 2:
        print("Usage: python program input.txt")
        sys.exit(1)
    elif ".txt" not in argv[1]:
        print("Input must be a txt file")
        sys.exit(1)
    
    groups = list()

    with open(argv[1]) as f:
        input = f.read()
        group = dict()
        group['size'] = 1
        for i, c in enumerate(input):
            if c == '\n':
                if input[i+1] == '\n':     #start a new group
                    groups.append(group)
                    group = dict()
                    group['size'] = 1
                elif i-1 > 0 and input[i-1].isalpha(): #count a groupmember
                    group['size'] += 1
            elif c.isalpha():         #add an answer to dictionary
                if c in group.keys():
                    group[c] += 1
                else: 
                    group[c] = 1                               
                if i+1 == len(input): #handle last group
                    groups.append(group)
    
    counta = 0
    for group in groups:
        counta += len(group)-1 # substract one as you shouldnt count the key 'groupsize'

    countb = 0
    for group in groups:
        for i in group:
            if i is not 'size' and group[i] == group['size']:
                countb += 1 

    print(f'Solution to a is {counta}')
    print(f'Solution to b is {countb}')
main()
             
