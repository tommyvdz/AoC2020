from sys import argv
import sys

def main():
    if len(argv) != 2:
        print("Usage: python program input.txt")
        sys.exit(1)
    elif ".txt" not in argv[1]:
        print("Input must be a txt file")
        sys.exit(1)

    treemap = list()
    with open(argv[1]) as f:
        input = f.readlines()
        for line in input:
            treerow = list()
            for char in line:
                treerow.append(char)
            treemap.append(treerow)
    slopes = [
        { 'x': 1,
          'y': 1},
        { 'x': 3,
          'y': 1},
        { 'x': 5,
          'y': 1},
        { 'x': 7,
          'y': 1},
        { 'x': 1,
          'y': 2}
    ]
    multiplied = 1
    for slope in slopes:
        trees = countTrees(treemap, slope)
        print(f'Trees encountered for slope {slope}: {trees}')
        multiplied *= trees
    print(f'Multiplied encountered trees: {multiplied}')        

def countTrees(map, slope):
    x = 0
    y = 0
    loc = 0
    treecount = 0
    while y < len(map):
        if map[y][x] == '\n':
            x = 0
        if map[y][x] == '#':
            treecount += 1
        if x+slope['x'] >= len(map[y]):
            x = (x+slope['x']) - (len(map[y])-1)
        else:
            x += slope['x']
        y += slope['y']    
    return treecount
main()


