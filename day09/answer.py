def parse_part1(lines):
    nums = []
    for line in lines:
        nums.append(int(line.strip()))
    return nums


def part1(lines):
    preamble = 25
    nums = parse_part1(lines)
    for i in range(preamble, len(nums)):
        if not has_sum(nums[i - preamble : i], nums[i]):
            return nums[i]
    return "LOL"

def has_sum(lst, num):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == num:
                return True
    return False

def part2(lines):
    invalid_num = part1(lines)
    nums = parse_part1(lines)
    min_i, max_i = find_range(nums, invalid_num)
    return min(nums[min_i: max_i + 1]) + max(nums[min_i: max_i + 1])

def find_range(nums, num):
    cont_set = []
    for i in range(len(nums) - 1):
        cont_set.append(nums[i])
        for j in range(i + 1, len(nums)):
            cont_set.append(nums[j])
            if sum(cont_set) == num:
                return i, j
            elif sum(cont_set) > num:
                break
        cont_set = []
    return

f = open("./input.txt", "r")
lines = f.readlines()

# print(part1(lines))
print(part2(lines))