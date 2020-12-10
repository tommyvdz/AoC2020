from sys import argv
import sys

def input():
    if len(argv) != 2:
        print("Usage: python program input.txt")
        sys.exit(1)
    elif ".txt" not in argv[1]:
        print("Input must be a txt file")
        sys.exit(1)

    input = list()
    
    with open(argv[1]) as f:
        input = f.readlines()
    
    return input