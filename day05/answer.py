def part1(lines):
    return max([eval_seat(l) for l in lines])

def part2(lines):
    seats = [eval_seat(l) for l in lines]
    small = min(seats)
    big = max(seats)
    for i in range(small, big+1):
        if i  not in seats:
            return i
    return 'LOL'

def eval_seat(l):
    first_half = l[0:7]
    second_half = l[7:10]

    row = 0
    to_pow = 6
    for char in first_half:
        char = char == 'B'
        row = row + char * 2 ** to_pow
        to_pow -= 1

    col = 0
    to_pow = 2
    for char in second_half:
        char = char == 'R'
        col = col + char * 2 ** to_pow
        to_pow -= 1
    
    return row * 8 + col

f = open("./input.txt", "r")

lines = [line.strip() for line in f.readlines()]
print(part2(lines))