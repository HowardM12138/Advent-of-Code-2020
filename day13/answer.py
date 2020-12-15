def part1(time_stamp, buses):
    time = time_stamp
    depart_time = list(filter(lambda x: time % x == 0, buses))
    while depart_time == []:
        time += 1
        depart_time = list(filter(lambda x: time % x == 0, buses))
    return (time - time_stamp) * depart_time[0]

def part2(buses):
    offset = [i for i in range(len(buses)) if buses[i] != 'x']
    buses_id = [x for x in buses if x != 'x']
    time = 0
    
    increment, first_num = find_diff(buses[:len(buses) // 3 * 2])
    print(increment, first_num)
    time = first_num

    def good_time(time):
        for i in range(len(offset)):
            if (time + offset[i]) % buses_id[i] != 0:
                return False
        return True

    while not good_time(time):
        time += increment
    
    return time + offset[0]

def find_diff(buses):
    max_bus = max(x for x in buses if x != 'x')
    max_bus_index = buses.index(max_bus)
    offset = [i - max_bus_index for i in range(len(buses)) if buses[i] != 'x']
    buses_id = [x for x in buses if x != 'x']
    time = 0
    
    increment = max_bus

    def good_time(time):
        for i in range(len(offset)):
            if (time + offset[i]) % buses_id[i] != 0:
                return False
        return True

    while not good_time(time):
        time += increment

    first_num = time + offset[0]

    time += increment
    while not good_time(time):
        time += increment
    
    return time + offset[0] - first_num, first_num

f = open("./input.txt", "r")

time_stamp = int(f.readline().strip())

buses = f.readline().strip().split(",")
for i in range(len(buses)):
    if buses[i] != "x":
        buses[i] = int(buses[i])
# print(part1(time_stamp, buses))

print(part2(buses))