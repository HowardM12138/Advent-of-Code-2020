def parse_part2(lines):
    relations = {}
    for line in lines:
        line = line.strip()
        args = line.split(" ")
        parent = args[0] + " " + args[1]
        childs = []
        for i in range(4, len(args)):
            arg = args[i]
            if arg == "no":
                break
            elif arg.isdigit():
                childs.append({args[i+1] + " " + args[i+2]: int(arg)})
        relations[parent] = childs
    return relations

def part2(lines):
    relations = parse_part2(lines)
    return seek_part2(relations, "shiny gold")

def seek_part2(relations, bag):
    count = 0
    for parent, child in relations.items():
        if bag == parent:
            for bag_dict in child:
                bag_name = list(bag_dict.keys())[0]
                bag_num = bag_dict[bag_name]
                count += (seek_part2(relations, bag_name) + 1) * bag_num
    return count

def part1(lines):
    relations = parse_part1(lines)
    return seek_part1(relations, 'shiny gold', [])

def seek_part1(relations, bag, seen):
    count = 0
    for parent, child in relations.items():
        if bag in child:
            if parent not in seen:
                seen.append(parent)
                count += 1 + seek_part1(relations, parent, seen)
    return count

def parse_part1(lines):
    relations = {}
    for line in lines:
        line = line.strip()
        args = line.split(" ")
        parent = args[0] + " " + args[1]
        childs = []
        for i in range(4, len(args)):
            arg = args[i]
            if arg == "no":
                break
            elif arg.isdigit():
                childs.append(args[i+1] + " " + args[i+2])
        relations[parent] = childs
    return relations

f = open("./input.txt", "r")
lines = f.readlines()

print(part1(lines))
print(part2(lines))