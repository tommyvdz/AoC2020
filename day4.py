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


    with open(argv[1]) as f:
        input = f.read()

    passports = readPassports(input)
    validpassports = 0
    for passport in passports:
        if checkValidity(passport):
            validpassports += 1
    print(validpassports)
    
def readPassports(file):
    inputfile = list()
    passports = list()
    for s in file.split("\n\n"):
        inputfile.append(s.split())
    for a,b in enumerate(inputfile):
        d = dict()
        for c in inputfile[a]:
            d.update({c[0:c.find(":")]: c[c.find(":")+1:]})
        passports.append(d)
    return passports

def countDigits(value):
    count = 0
    for c in value:
        if c.isdigit():
            count += 1
        if not c.isdigit():
            break
    return count

def byr(value):
    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if countDigits(value) == 4 and int(value) in range(1920,2003):
        return True
    return False

def iyr(value):
   # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if countDigits(value) == 4 and int(value) in range(2010,2021):
        return True
    return False

def eyr(value):
    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if countDigits(value) == 4 and int(value) in range(2020,2031):
        return True
    return False

def hgt(value):
#     hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
    number = int(''.join(list(filter(lambda c: c.isdigit(), value))))
    measure = ''.join(list(filter(lambda c: c.isalpha(), value)))
    if measure == 'cm' and number in range(150,194):
        return True
    elif measure == 'in' and number in range(59,77):
        return True
    return False

def hcl(value):
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value)
    if match:
        return True 
    return False

def ecl(value):
#    exactly one of: amb blu brn gry grn hzl oth.
    if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False

def pid(value):
#    pid (Passport ID) - a nine-digit number, including leading zeroes.
    if countDigits(value) == 9:
        return True
    return False

def validateData(key, value):
    switcher = {
        'byr': byr,
        'iyr': iyr,
        'eyr': eyr,
        'hgt': hgt,
        'hcl': hcl,
        'ecl': ecl,
        'pid': pid,
    }
    func = switcher.get(key, lambda x: False)
    return func(value)



def checkValidity(passport):
    mandatoryfields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for k in mandatoryfields:
        if not k in passport:
            return False
        if not validateData(k, passport[k]):
            return False
    return True

main()
