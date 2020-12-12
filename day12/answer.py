def part1(steps):

    x = 0
    y = 0
    direction = (1, 0)

    def process(action, value):
        nonlocal x, y, direction
        if action == 'N':
            y += value
        elif action == 'S':
            y += -1 * value
        elif action == 'E':
            x += value
        elif action == 'W':
            x += -1 * value
        elif action == 'L':
            if value == 90:
                direction = (direction[1] * -1, direction[0])
            elif value == 180:
                direction = (direction[0] * -1, direction[1] * -1)
            elif value == 270:
                direction = (direction[1], -1 * direction[0])
            else:
                print(value)
        elif action == 'R':
            if value == 90:
                direction = (direction[1], -1 * direction[0])
            elif value == 180:
                direction = (direction[0] * -1, direction[1] * -1)
            elif value == 270:
                direction = (direction[1] * -1, direction[0])
        elif action == "F":
            x += direction[0] * value
            y += direction[1] * value
        
    for step in steps:
        process(step[0], step[1])
    
    return abs(x) + abs(y)


def part2(steps):

    x_waypoint = 10
    y_waypoint = 1
    x = 0
    y = 0

    def process(action, value):
        nonlocal x, y, x_waypoint, y_waypoint
        if action == 'N':
            y_waypoint += value
        elif action == 'S':
            y_waypoint += -1 * value
        elif action == 'E':
            x_waypoint += value
        elif action == 'W':
            x_waypoint += -1 * value
        elif action == 'L':
            if value == 90:
                x_waypoint, y_waypoint = y_waypoint * -1, x_waypoint
            elif value == 180:
                x_waypoint, y_waypoint = x_waypoint * -1, y_waypoint * -1
            elif value == 270:
                x_waypoint, y_waypoint = y_waypoint, x_waypoint * -1
            else:
                print(value)
        elif action == 'R':
            if value == 90:
                x_waypoint, y_waypoint = y_waypoint, x_waypoint * -1
            elif value == 180:
                x_waypoint, y_waypoint = x_waypoint * -1, y_waypoint * -1
            elif value == 270:
                x_waypoint, y_waypoint = y_waypoint * -1, x_waypoint
            else:
                print(value)
        elif action == "F":
            x += x_waypoint * value
            y += y_waypoint * value

    for step in steps:
        process(step[0], step[1])

    return abs(x) + abs(y)

f = open("./input.txt", "r")
lines = f.readlines()

steps = []
for line in lines:
    line = line.strip()
    steps.append((line[0], int(line[1:])))

# print(part1(steps))
print(part2(steps))