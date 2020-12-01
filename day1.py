from sys import argv
import sys

def main():
    if len(argv) != 2:
        print("Usage: python program input.txt")
        sys.exit(1)
    elif ".txt" not in argv[1]:
        print("Input must be a txt file")
        sys.exit(1)

    with open(argv[1]) as f:
        inputs = f.readlines()
        input = [int(x) for x in inputs]
        a = 0
        b = 0
        for x in input:
            num2 = 2020 - x
            if num2 in input and a == 0:
                a = x * num2
                print(f'Answer a is: {a}')
            for y in input:
                num1 = num2 - y
                if (b == 0 and num1 in input):
                    b = x * y * num1
                    print(f'Answer b is: {b}')

main()
