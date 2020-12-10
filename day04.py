"""
Day 4: Passport Processing
Url = https://adventofcode.com/2020/day/4
"""
import re

with open('inputs/input4.txt') as file:
    passports = file.read()

passports = passports.split('\n\n')

# --- Part A --- #
valids = 0

for passport in passports:
    if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport:
        if 'hcl' in passport and 'ecl' in passport and 'pid' in passport:
            valids += 1

print(valids)

# --- Part B --- #
with open('inputs/input4.txt') as file:
    passports = file.read()

passports = passports.split('\n\n')
dictionary = {'byr':0, 'iyr':0, 'eyr':0, 'hgt':'', 'hcl':'', 'ecl':'', 'pid':''}
valids = 0

def ishex(s):
    for c in s:
        if c not in string.hexdigits:
            return False

    return True

def validate_passport(passport):
    if not 1920 <= int(passport['byr']) <= 2002:
        return False

    if not 2010 <= int(passport['iyr']) <= 2020:
        return False

    if not 2020 <= int(passport['eyr']) <= 2030:
        return False

    if not ((passport['hgt'][-2:] == 'in' and 59 <= int(passport['hgt'][:-2]) <= 76) or (passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 193)):
        return False

    if not (len(passport['hcl']) == 7 and passport['hcl'][0] == '#' and ishex(passport['hcl'][1:0])):
        return False

    if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if not (len(passport['pid']) == 9 and passport['pid'].isnumeric()):
        return False

    return True

for passport in passports:
    passport = re.split('\n| ', passport)
    for data in passport:
        data = data.split(':')
        dictionary[data[0]] = data[1]

    valid =  validate_passport(dictionary)

    if valid == True:
        valids += 1

    dictionary = {'byr':0, 'iyr':0, 'eyr':0, 'hgt':'', 'hcl':'', 'ecl':'', 'pid':''}

print(valids)
