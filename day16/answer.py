def part1(lines):
    ranges, tickets = parse_part1(lines)
    valid_tickets = []

    def valid(x):
        for range in ranges:
            if (range[0] <= x <= range[1]):
                return True
        return False

    for ticket in tickets:
        valid_ticket = True
        for num in ticket:
            if not valid(num):
                valid_ticket = False
                break
        if valid_ticket:
            valid_tickets.append(ticket)
    
    return valid_tickets

def parse_part1(lines):
    ranges = []
    tickets = []
    for line in lines:
        line = line.strip()
        if line != "":
            if "or" in line:
                line = line.split(": ")[1].split(" or ")
                range1, range2 = line[0].split("-"), line[1].split("-")
                ranges.append((int(range1[0]), int(range1[1])))
                ranges.append((int(range2[0]), int(range2[1])))
            else:
                tickets.append([int(x) for x in line.split(",")])
    return ranges, tickets

def part2(tickets, lines):
    fields = get_fields(lines)

    for col in range(len(fields)):
        for ticket in tickets:
            num = ticket[col]
            for field in fields:
                return


def get_fields(lines):
    fields = {}
    for line in lines:
        line = line.strip()
        if line == "":
            break
        else:
            line = line.split(": ")
            field_name = line[0]
            ranges = line[1]
            ranges = ranges.split(" or ")
            range1, range2 = ranges[0].split("-"), ranges[1].split("-")
            ranges = []
            ranges.append((int(range1[0]), int(range1[1])))
            ranges.append((int(range2[0]), int(range2[1])))
            fields[field_name] = ranges
    return fields


f = open("./input1.txt", "r")
lines = f.readlines()

valid_tickets = part1(lines)
print(part2(valid_tickets, lines))