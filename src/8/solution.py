#advent code challenge day 4 problem 2

import sys
import re

REQUIRED_KEYS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]

EYE_COLORS = [
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth"
]

HCL_REGEX = re.compile('#([0-9a-f]+)')

def parse_passport(entry):
    passport = {}
    for field in entry.split():
        [key, val] = field.split(':')
        passport[key] = val
    return passport

def is_not_valid_height(height):
    size = int(height[:len(height) - 2])
    if height[len(height) - 1] == 'm':
        if size < 150 or size > 193:
            return True
    else:
        if size < 59 or size > 76:
            return True
    return False

def is_not_valid_haircolor(haircolor):
    matches = HCL_REGEX.fullmatch(haircolor)
    return (matches is None)

def is_valid_passport(passport):
    if any(key not in passport for key in REQUIRED_KEYS):
        return False
    if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        return False
    if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        return False
    if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        return False
    if is_not_valid_height(passport["hgt"]):
        return False
    if is_not_valid_haircolor(passport["hcl"]):
        return False
    if passport["ecl"] not in EYE_COLORS:
        return False
    if len(passport["pid"]) != 9:
        return False
    return True

with open(sys.argv[1]) as f:
    entries = f.read().split("\n\n")
    passports = [parse_passport(entry) for entry in entries]

    valid_passports_count = 0
    for passport in passports:
        if is_valid_passport(passport):
            valid_passports_count += 1

    print(valid_passports_count)