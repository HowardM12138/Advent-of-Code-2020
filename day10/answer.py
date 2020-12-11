from functools import lru_cache

def parse_part1(lines):
    nums = []
    for line in lines:
        nums.append(int(line.strip()))
    nums.sort()
    return nums

def part1(lines):
    adaptors = parse_part1(lines)
    previous_volt = 0
    volt_diff1 = 0
    volt_diff2 = 0
    volt_diff3 = 0
    while adaptors != []:
        adaptor = find_next(adaptors, previous_volt)
        if adaptor - previous_volt == 1:
            volt_diff1 += 1
        elif adaptor - previous_volt == 3:
            volt_diff3 += 1
        else:
            volt_diff2 += 1
        adaptors.remove(adaptor)
        previous_volt = adaptor
    volt_diff3 += 1
    return volt_diff3 * volt_diff1
    
def part2(lines):
    adaptors = parse_part1(lines)
    @lru_cache(None)
    def helper(index, previous_volt):
        if index == len(adaptors):
            return 1
        else:
            possible_adaptors = [x for x in adaptors[index:min(len(adaptors), index+3)] if x - previous_volt <= 3]
            count = 0
            for i in range(len(possible_adaptors)):
                adaptor = possible_adaptors[i]
                count += helper(index + i+1, adaptor)
            return count
    return helper(0, 0)
    
def find_next(lst, num):
    return min(filter(lambda x: x - num <= 3, lst))


f = open("./input.txt", "r")
lines = f.readlines()

# print(part1(lines))
print(part2(lines))