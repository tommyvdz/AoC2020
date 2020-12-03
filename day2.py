from sys import argv
import sys

def main():
    if len(argv) != 2:
        print("Usage: python program input.txt")
        sys.exit(1)
    elif ".txt" not in argv[1]:
        print("Input must be a txt file")
        sys.exit(1)

    validpasswordsA = 0
    validpasswordsB = 0

    with open(argv[1]) as f:
        inputs = f.readlines()
        for line in inputs:
            if isPasswordValidOldPolicy(line):
                validpasswordsA += 1
            if isPasswordValidNewPolicy(line):
                validpasswordsB += 1
        print(f'Answer A is: {validpasswordsA}')
        print(f'Answer B is: {validpasswordsB}')

def isPasswordValidOldPolicy(input): 
    counter = 0
    left = input[0:input.index(":")]
    right = input[input.index(':')+2:]
    if left[1].isdigit():
        min = int(left[0] + left[1])
    else:
        min = int(left[0])
    if left[left.index("-")+2].isdigit():
        max = int(left[left.index("-")+1] + left[left.index("-")+2])
    else:
        max = int(left[left.index("-")+1])
    value = left[left.index(" ")+1]
    for c in right:
        if c == value:
            counter += 1
    if counter in range(min, max+1):
        return True
    else:
        return False

def isPasswordValidNewPolicy(input): 
    left = input[0:input.index(":")]
    right = input[input.index(':')+2:]
    if left[1].isdigit():
        pos1 = int(left[0] + left[1])
    else:
        pos1 = int(left[0])
    if left[left.index("-")+2].isdigit():
        pos2 = int(left[left.index("-")+1] + left[left.index("-")+2])
    else:
        pos2 = int(left[left.index("-")+1])
    value = left[left.index(" ")+1]
    if pos2 > len(right):
        if value is right[pos1-1]:
            return True
    elif value is right[pos1-1] and value is right[pos2-1]:
        return False
    elif value is right[pos1-1]:
        return True
    elif value is right[pos2-1]:
        return True
    else:
        return False

main()
