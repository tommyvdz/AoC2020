import app

def main():
    input = app.input()
    print(solve1(input))
    print(solve2(input))

    # for line in input:
    #     instr[line[0]] = int(line[1:])
    # print(instr)

def solve1(instr: list):
    direction = 'E'
    east = 0
    west = 0
    north = 0
    south = 0
    for line in instr:
        if line[0] == 'F':
            if direction == 'N':
                north += int(line[1:])
            if direction == 'S':
                south += int(line[1:])
            if direction == 'E':
                east += int(line[1:])
            if direction == 'W':
                west += int(line[1:])
        elif line[0] == 'N':
            north += int(line[1:])
        elif line[0] == 'S':
            south += int(line[1:])
        elif line[0] == 'E':
            east += int(line[1:])
        elif line[0] == 'W':
            west += int(line[1:])
        elif line[0] == 'R':
            direction = getDirection(int(line[1:]), direction)
        elif line[0] == 'L':
            direction = getDirection(-int(line[1:]), direction)
        else:
            print(f'Error for {line}')
    eastwest = west-east
    northsouth = north-south
    return abs(eastwest + northsouth)

def solve2(instr: list):
    waypoint = {'ns': 1, 'ew':10}
    ship = {'ns': 0, 'ew': 0}
    for line in instr:
        if line[0] == 'F':
            ship['ns'] += int(line[1:])*waypoint['ns']
            ship['ew'] += int(line[1:])*waypoint['ew']       
        elif line[0] == 'N':
            waypoint['ns'] += int(line[1:])
        elif line[0] == 'S':
            waypoint['ns'] -= int(line[1:])
        elif line[0] == 'E':
            waypoint['ew'] += int(line[1:])
        elif line[0] == 'W':
            waypoint['ew'] -= int(line[1:])
        elif line[0] in ['L', 'R']:
            waypoint = rotate(waypoint, line[:len(line)-1])
        else:
            print(f'Error for {line}')

    return abs(ship['ew']) + abs(ship['ns'])

def getDirection(degree, currentdirection):
    dirs = ['N', 'E', 'S', 'W']
    cdegree = dirs.index(currentdirection)
    ix = round(degree / (360. / len(dirs)))
    return dirs[(ix+cdegree) % len(dirs)]


# https://en.wikipedia.org/wiki/Rotation_matrix
rotations = { 
    "R90": [[0, 1], [-1, 0]],  "R180": [[-1, 0], [0, -1]], "R270": [[0,-1], [1,0]],
    "L90": [[0,-1], [1,0]], "L180": [[-1, 0], [0, -1]], "L270": [[0, 1], [-1, 0]]
}    
def rotate(waypoint, deg):
    r = rotations[deg]
    x = waypoint['ew']
    y = waypoint['ns']
    waypoint['ew'] = x*r[0][0] + y*r[0][1]
    waypoint['ns'] = x*r[1][0] + y*r[1][1]
    return waypoint


main()