# day 7 problem 1
import sys

# parse_bag_definition("dotted blue bags contain 5 wavy green bags, 3 pale beige bags.")
# => ("dotted blue", { "wavy green", "pale beige" })
def parse_bag_definition(text):
    result = text.split("bags contain")
    bag_name = result[0].strip()
    children = set()

    if 'no other bags' not in result[1]:
        for each_bag in result[1].split(","):
            parts = each_bag.strip().split()
            children.add(f'{parts[1]} {parts[2]}')

    return (bag_name, children)

bag_map = {}
with open(sys.argv[1]) as f:
    for line in f:
        (parent, children) = parse_bag_definition(line)

        for child in children:
            if child not in bag_map:
                bag_map[child] = set()
            bag_map[child].add(parent)

# find all bags that could contain "shiny gold"
bags = set()
bags_to_search = { "shiny gold" }

while len(bags_to_search) > 0:
    found_bags = set()
    for bag_to_search in bags_to_search:
        if bag_to_search not in bag_map:
            continue
        for child in bag_map[bag_to_search]:
            if child not in bags:
                found_bags.add(child)
                bags.add(child)
    bags_to_search = found_bags

print(len(bags))