def part1(lines):
    turn = 0
    starting_nums = parse_part1(lines)
    stack = {}
    last_spoken = 0
    while turn < 30000000:
        turn += 1
        if starting_nums:
            last_spoken = starting_nums[0]
            starting_nums = starting_nums[1:]
        else:
            i = stack[last_spoken]
            first_i = i[0]
            second_i = i[1]
            if second_i == None:
                last_spoken = 0
            else:
                last_spoken = first_i - second_i
        if last_spoken in stack.keys():
            i = stack[last_spoken]
            i[1] = i[0]
            i[0] = turn
            stack[last_spoken] = i
        else:
            stack[last_spoken] = [turn, None]
    return last_spoken

def parse_part1(lines):
    line = lines[0].strip()
    nums = []
    for num in line.split(','):
        nums.append(int(num))
    return nums


f = open("./input.txt", "r")

print(part1(f.readlines()))
# print(part2(f.readlines()))