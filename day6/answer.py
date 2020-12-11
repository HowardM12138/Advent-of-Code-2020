def part1(lines):
    total = 0
    for line in lines:
        count = 0
        existing = []
        for char in line:
            if char != " " and char not in existing:
                count += 1
                existing.append(char)
        total += count
    return total

def part2(lines):
    total = 0
    for group in lines:
        responses = group.split(' ')
        tally = {}
        for response in responses:
            for char in response:
                if char not in tally:
                    tally[char] = 1
                else:
                    tally[char] += 1
        total_count = len(responses)
        count = 0
        for key in tally:
            if tally[key] == total_count:
                count += 1
        total += count
    return total

f = open("./input.txt", "r")

lines = []
l = ''
for line in f.readlines():
    line = line.strip()
    if line == '':
        lines.append(l[:-1])
        l = ''
    else:
        l = l + line + ' '
lines.append(l[:-1])

print(part2(lines))