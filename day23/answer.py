def part1(nums):
    c_i = 0

    def p_i(i, l):
        while i >= l:
            i = i - l
        return i

    def move():
        nonlocal nums, c_i
        print("current num", nums[c_i])
        if c_i >= len(nums) - 3:
            nums = nums[c_i:] + nums[:c_i]
            c_i = 0
        temp_nums = nums[:c_i+1] + nums[c_i+4:]
        picked_nums = nums[c_i+1:c_i+4]
        current_num = nums[c_i]
        destinate_num = nums[c_i] - 1
        while destinate_num in picked_nums or destinate_num not in temp_nums:
            destinate_num -= 1
            if destinate_num < min(nums):
                destinate_num = max(nums)
        d_i = temp_nums.index(destinate_num)
        print(destinate_num, picked_nums)
        nums = temp_nums[:d_i+1] + picked_nums + temp_nums[d_i+1:]
        c_i = p_i(nums.index(current_num) + 1, len(nums))
    
    for _ in range(100):
        print(nums)
        move()
        
    i = nums.index(1)
    nums = nums[i+1:] + nums[:i]
    return "".join([str(n) for n in nums])


line = open("./input.txt", "r").readlines()[0].strip()

nums = [int(n) for n in line]

print(part1(nums))