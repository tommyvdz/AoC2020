import app
import copy

def main():
    input = app.input()

    seats = []
    for line in input:
        seats.append(list(line.strip()))
    part1 = 0
    
    i=1
    seatsa = copy.deepcopy(seats)
    while i != part1:
        i = part1
        seatsa = arrangePart1(seatsa)
        part1 = countSeats(seatsa)
    print(f'Part1: {part1}')

    part2 = 0
    j=1
    seatsb = copy.deepcopy(seats)
    while j != part2:
        j = part2
        seatsb = arrangePart2(seatsb)
        part2 = countSeats(seatsb)
    print(f'Part2: {part2}')

def lookFurther(seats, i, i2, h, v):
    i += v
    i2 += h
    while i >= 0 and i < len(seats) and i2 >= 0 and i2 < len(seats[i]):
        if seats[i][i2] == '#':
            return 1
        if seats[i][i2] == 'L':
            return 0
        i += v
        i2 += h
    return 0
    

def arrangePart1(seats):
    newseats = copy.deepcopy(seats)
    for i, row in enumerate(seats):
        for i2, seat in enumerate(seats[i]):
            if seat != '.':
                horizontal = range(-1,2)
                vertical = range(-1,2)
                if i == 0: #don't check above
                    vertical = range(0,2)
                if i2 == 0: # don't check left
                    horizontal = range(0,2)
                if i2 == len(seats[i])-1: #don't check right
                    horizontal = range(-1,1)
                if i == len(seats)-1: #don't check below
                    vertical = range(-1,1)
                occupied = 0
                for h in horizontal:
                    for v in vertical:
                       # print(f'for {i},{i2} I am looking at Horizontal {h} and Vertical {v}')
                        if v == 0 and h == 0:
                            continue
                        if seats[i+v][i2+h] == '#':
                            occupied += 1
                if occupied == 0:
                    newseats[i][i2] = '#'
                if seats[i][i2] == '#' and occupied >= 4:
                    newseats[i][i2] = 'L'
    return newseats

def arrangePart2(seats):
    newseats = copy.deepcopy(seats)
    for i, row in enumerate(seats):
        for i2, seat in enumerate(seats[i]):
            if seat != '.':
                horizontal = range(-1,2)
                vertical = range(-1,2)
                if i == 0: #don't check above
                    vertical = range(0,2)
                if i2 == 0: # don't check left
                    horizontal = range(0,2)
                if i2 == len(seats[i])-1: #don't check right
                    horizontal = range(-1,1)
                if i == len(seats)-1: #don't check below
                    vertical = range(-1,1)
                occupied = 0
                for h in horizontal:
                    for v in vertical:
                       # print(f'for {i},{i2} I am looking at Horizontal {h} and Vertical {v}')
                        if v == 0 and h == 0:
                            continue
                        if seats[i+v][i2+h] == '#':
                            occupied += 1
                        if seats[i+v][i2+h] == '.':
                            occupied += lookFurther(seats,i,i2,h,v)
                if occupied == 0:
                    newseats[i][i2] = '#'
                if seats[i][i2] == '#' and occupied >= 5:
                    newseats[i][i2] = 'L'
    return newseats

def countSeats(seats):
    count = 0
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == '#':
                count += 1
    return count

def printSeats(seats):
    print('----------------------------------')
    for i in range(len(seats)):
        print(f'{i}:{seats[i]}')


main()
