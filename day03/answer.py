f = open("./input.txt", "r")

lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')

i = 0
j = 0
count = 0

while i != len(lines) - 1:
    i += 1
    j += 3

    if j >= len(lines[i]):
        j -= len(lines[i])
    if lines[i][j] == "#":
        count += 1

print(count)