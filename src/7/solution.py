# advent code challenge day 4 problem 1

import sys

REQUIRED_KEYS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]

# example of an entry:
#
# hcl:#6b5442 ecl:brn iyr:2019
# pid:637485594 hgt:171cm
# eyr:2021 byr:1986
def parse_passport(entry):
    passport = {}
    for field in entry.split():
        [key, val] = field.split(':')
        passport[key] = val
    return passport

def is_valid_passport(passport):
    return all(key in passport for key in REQUIRED_KEYS)

with open(sys.argv[1]) as f:
    entries = f.read().split("\n\n")
    passports = [parse_passport(entry) for entry in entries]

    valid_passports_count = 0
    for passport in passports:
        if is_valid_passport(passport):
            valid_passports_count += 1

    print(valid_passports_count)

'''
foo = ["a", "3"]
bar = {}
bar[foo] = "apple"

names = ["mukund", "siddharth", "tom", "nancy", ...] # 100000000 names!
[len(name) < 25 for name in names]
all(len(name) < 25 for name in names)

# this is what bar looks like:
#
# { ["a", "3"]: "apple" }

foo in bar

grades = { "mukund": 75, "siddharth": 100, "tom": 80, "nancy": 10 }
students = ["siddharth", "tom", "nancy"]

names = []
for name in students:
    names.append(name)
names

[name in grades for name in students]
[True, True, True]

if all(name in grades for name in students):
    # whatever

my_keys = ["a", "b", "c"]
my_map = { "a": "something"}
"a" in my_map # False
'''