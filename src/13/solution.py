# day 7 problem 1
import sys

# parse_bag_definition("dotted blue bags contain 5 wavy green bags, 3 pale beige bags.")
# => ("dotted blue", { "wavy green", "pale beige" })
def parse_bag_definition(text):
    result = text.split("bags contain")
    bag_name = result[0].strip()
    contained_bags = set()

    if 'no other bags' not in result[1]:
        for each_bag in result[1].split(","):
            parts = each_bag.strip().split()
            contained_bags.add(f'{parts[1]} {parts[2]}')

    return (bag_name, contained_bags)

bag_map = {}
with open(sys.argv[1]) as f:
    for line in f:
        t = parse_bag_definition(line)
        bag_map[t[0]] = t[1]

current_bags = set()
next_bags = set()
exhausted_bags = set()

current_bags.add("shiny gold")

while(len(current_bags) != 0):
    for key, value in bag_map.items():
        if len(set.intersection(current_bags, value)) > 0 and key not in exhausted_bags:
            next_bags.add(key)
            exhausted_bags.add(key)
    current_bags = next_bags.copy()
    next_bags.clear()

print(len(exhausted_bags))

# list_a = [[0, 1]]
# list_b = list_a.copy()
# list_a[0].clear()
# print(len(list_b[0])) # what should this be?

# list_a --- 0x1234 => [[0,1]] => [length = 1, [0,1]]

# 0xdef => [ 0x123 ]

# 0x123 => [ 0xdef, b, c ]
# 0xabc => [ 0xfed, b, c ]

# [ 0x123, 0x456, 0x789 ]
# shallow copy: new_array = [ 0x123, 0x456, 0x789 ]
# deep copy: [ 0xabc ]

# shop = [blue_deck, list_b, list_c]
# blue_deck_copy = [item for item in blue_deck]
# ash = [blue_deck_copy]

# shallow copy memory example #############################
# list_a --- 0x1234 => [ 0x5678 ] => [length = 1, [0x5678]]
# list_b --- 0x4321 => [ 0x5678 ] => ""
# list_a.clear()
# list_a --- 0x1234 => []         => [length = 0, [0x5678]]
# list_b --- 0x4321 => [ 0x5678 ] => [length = 1, [0x5678]]

# { name: "Charizard", hp: 100 }
# 0x5678 => [ 0x9123 ] 
#            0x5678 => [0x9123, 1] => [length = 2, [{stuff}, 1]]

# print(count)

# my_set.pop()

# next_bags ====\ 
#                --- 0x1234 => {} => [length = 0, "bright red"]
# current_bags =/ 

'''
    dictionary = {bag, contained_bags}
    new_bags initially is shiny gold
    while (new_bags is not empty)
        search dictionary for keys associated with new_bags
        new_bags = keys
        count += number of new_bags
'''