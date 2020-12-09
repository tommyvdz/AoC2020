from sys import argv
import sys
import re

def main():
    if len(argv) != 2:
        print("Usage: python program input.txt")
        sys.exit(1)
    elif ".txt" not in argv[1]:
        print("Input must be a txt file")
        sys.exit(1)

    bags = dict()

    with open(argv[1]) as f:
        input = f.readlines()
        for line in input:
            finput = re.split("\s|(?<!\d)[,.](?!\d)", line)
            for i, word in enumerate(finput):  
                if word == "contain":
                    container = (finput[i-3]+" "+finput[i-2])
                    bags.update({container: list()})
                if word.isdigit():
                    bags[container].append({(finput[i+1]+" "+finput[i+2]): int(word)})
        counter = 0
        target = 'shiny gold'
        amount = 0
        for bag in bags:
            if containsShinygold(target, bag, bags):
                counter += 1
        amount = howManyBags(target, bags)
        print(f'counter for {target} is {counter}')
        print(f'amount for {target} is {amount}')

def containsShinygold(target, bag, bags):
    for i in bags[bag]:
        for x in i:
            if target == x:
                return True
            if containsShinygold(target, x, bags):
                return True
    return False

def howManyBags(target, bags):
    amount = 0
    bagcontents = bags.get(target)
    for i in bagcontents:
        for x in i:
            if howManyBags(x, bags) == 0:
                amount += i[x] * 1
            else:
                amount += i[x] + (i[x] * howManyBags(x, bags))
    return amount

main()

