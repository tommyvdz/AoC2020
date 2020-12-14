import app

def main():
    input = app.input()
    deptime = int(input[0])
    busses = [int(item) if item != 'x' else item for item in input[1].split(',')]
    print(solve1(deptime, busses))
    print(solve2(busses))

def solve1(deptime, busses):
    multiplied = []
    for bus in busses:
        if bus != 'x':
            multiplied.append(multiplier(bus, deptime))
        else:
            multiplied.append(deptime*9999) #workaround to put the x in the array while preventing it from messing up the rest of the logic
    wait = min(multiplied) - deptime
    return busses[multiplied.index(min(multiplied))] * wait

def multiplier(value, max):
    result = value
    while result < max:
        result += value
    return result

def solve2(busses):
    tempdict = { i : busses[i] for i in range(0, len(busses) ) }
    resultdict = {}
    for key, value in tempdict.items():
        if value != 'x':
            resultdict[key] = value
    loop = True
    t = 0
    while loop:
        t += resultdict[0]
        result = 0
        for key, value in resultdict.items():
            result += (t + key) % busses[key] 
        if result == 0:
            return t
    return t
            
main()