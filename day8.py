from sys import argv
import sys
from copy import deepcopy

def main():
    if len(argv) != 2:
        print("Usage: python program input.txt")
        sys.exit(1)
    elif ".txt" not in argv[1]:
        print("Input must be a txt file")
        sys.exit(1)

    program = list(dict())

    with open(argv[1]) as f:
        input = f.readlines()
        for line in input:
            key = line.split()[0]
            value = int(line.split()[1])
            program.append({key: value})
    
    acc = runProgram(program)
    i = 0
    copy = deepcopy(program)
    possiblechanges = []
    for i, l in enumerate(program):
        if 'jmp' in l.keys() or 'nop' in l.keys():
            possiblechanges.append(i)
    for i in possiblechanges:
        copy = deepcopy(program)
        acc = alterInstruction(copy, i)
        if acc[1] == 0:
            print(f'Result acc value is {acc} (read 0 as exitcode 0)')
            print(f'changed value at position {i} which was {program[i]}')
            exit(0)
    print(f'Didnt find correct value acc')

def alterInstruction(program, i):
    acc = 0
    pos = 0
    if 'nop' in program[i].keys():
        program[i]['jmp'] = program[i].pop('nop')
    if 'jmp' in program[i].keys():
        program[i]['nop'] = program[i].pop('jmp')
    acc = runProgram(program)
    return acc


def runProgram(program):
    history = list()
    acc = 0
    pos = 0
    while pos < len(program):
        if pos in history:
            return [acc, 1]   
        history.append(pos)
        inst = program[pos]
        if 'nop' in inst.keys():
            pos += 1
            continue
        if 'jmp' in inst.keys():
            pos += inst['jmp']
            continue
        if 'acc' in inst.keys():
            acc += inst['acc']
            pos += 1
            continue
    return [acc, 0]
main()
    
    
