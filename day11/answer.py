def part1(seats):
    seat_change = True
    to_change = []
    while seat_change:
        seat_change = False
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                if seats[i][j] == "L" and not count_occupy(seats, i, j):
                    to_change.append([i,j])
                if seats[i][j] == "#" and count_occupy(seats, i, j) >= 4:
                    to_change.append([i,j])
        for coord in to_change:
            x = coord[0]
            y = coord[1]
            if seats[x][y] == "L":
                seats[x] = seats[x][:y] + "#" + seats[x][y+1:]
            elif seats[x][y] == "#":
                seats[x] = seats[x][:y] + "L" + seats[x][y+1:]
        if len(to_change) != 0:
            seat_change = True
            to_change = []
    return sum(sum(seat == "#" for seat in row) for row in seats)

def part2(seats):
    seat_change = True
    to_change = []
    while seat_change:
        seat_change = False
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                if seats[i][j] == "L" and not count_occupy_part2(seats, i, j):
                    to_change.append([i,j])
                if seats[i][j] == "#" and count_occupy_part2(seats, i, j) >= 5:
                    to_change.append([i,j])
        for coord in to_change:
            x = coord[0]
            y = coord[1]
            if seats[x][y] == "L":
                seats[x] = seats[x][:y] + "#" + seats[x][y+1:]
            elif seats[x][y] == "#":
                seats[x] = seats[x][:y] + "L" + seats[x][y+1:]
        if len(to_change) != 0:
            seat_change = True
            to_change = []
    return sum(sum(seat == "#" for seat in row) for row in seats)

def count_occupy_part2(seats, i, j):
    count = 0
    
    #left
    for c in range(j - 1, -1, -1):
        if seats[i][c] == "#":
            count += 1
            break
        elif seats[i][c] == "L":
            break

    #right
    for c in range(j + 1, len(seats[0])):
        if seats[i][c] == "#":
            count += 1
            break
        elif seats[i][c] == "L":
            break
    
    #up
    for r in range(i - 1, -1, -1):
        if seats[r][j] == "#":
            count += 1
            break
        elif seats[r][j] == "L":
            break
    
    #down
    for r in range(i + 1, len(seats)):
        if seats[r][j] == "#":
            count += 1
            break
        elif seats[r][j] == "L":
            break

    #left-up
    r = i - 1
    c = j - 1
    while 0 <= r < len(seats) and 0 <= c < len(seats[0]):
        if seats[r][c] == "#":
            count += 1
            break
        elif seats[r][c] == "L":
            break
        r -= 1
        c -= 1

    #right-up
    r = i - 1
    c = j + 1
    while 0 <= r < len(seats) and 0 <= c < len(seats[0]):
        if seats[r][c] == "#":
            count += 1
            break
        elif seats[r][c] == "L":
            break
        r -= 1
        c += 1

    #left-down
    r = i + 1
    c = j - 1
    while 0 <= r < len(seats) and 0 <= c < len(seats[0]):
        if seats[r][c] == "#":
            count += 1
            break
        elif seats[r][c] == "L":
            break
        r += 1
        c -= 1

    #right-down
    r = i + 1
    c = j + 1
    while 0 <= r < len(seats) and 0 <= c < len(seats[0]):
        if seats[r][c] == "#":
            count += 1
            break
        elif seats[r][c] == "L":
            break
        r += 1
        c += 1

    return count

def count_occupy(seats, i, j):
    coords = [
        [i - 1, j - 1], 
        [i - 1, j],
        [i - 1, j + 1],
        [i, j - 1],
        [i , j + 1],
        [i + 1, j - 1],
        [i + 1, j],
        [i + 1, j + 1]
        ]
    count = 0
    for coord in coords:
        x = coord[0]
        y = coord[1]
        if 0 <= x < len(seats) and 0 <= y < len(seats[0]) and seats[x][y] == "#":
            count += 1
    return count

f = open("./input.txt", "r")
lines = f.readlines()

seats = []
for line in lines:
    seats.append(line.strip())

# print(part1(seats))
print(part2(seats))