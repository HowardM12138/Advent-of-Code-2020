def part1_parse(lines):
    ins = []
    for line in lines:
        line = line.strip()
        arg, val = line.split(" ")
        if val[0] == "+":
            val = int(val[1:])
        elif val[0] == "-":
            val = int(val[1:]) * -1
        else:
            val = 0
        ins.append([arg, val])
    return ins 


def part1(lines):
    ins = part1_parse(lines)
    index_history = []
    index = 0
    acc = 0
    while index not in index_history:
        index_history.append(index)
        arg, val = ins[index][0], ins[index][1]
        if arg == "nop":
            index += 1
        elif arg == "acc":
            acc += val
            index += 1
        else:
            index += val
    return acc

def check_inf(ins):
    index_history = []
    index = 0
    acc = 0
    while index < len(ins) and index not in index_history:
        index_history.append(index)
        arg, val = ins[index][0], ins[index][1]
        if arg == "nop":
            index += 1
        elif arg == "acc":
            acc += val
            index += 1
        else:
            index += val
    return index == len(ins), acc


def part2(lines):
    ins = part1_parse(lines)
    acc = 0
    for i in range(len(ins)):
        if ins[i][0] == "nop":
            ins[i][0] = "jmp"
            terminate, acc = check_inf(ins)
            if terminate:
                return acc
            else:
                ins[i][0] = "nop"
        elif ins[i][0] == "jmp":
            ins[i][0] = "nop"
            terminate, acc = check_inf(ins)
            if terminate:
                return acc
            else:
                ins[i][0] = "jmp"
    return "LOL"

    


f = open("./input.txt", "r")
lines = f.readlines()

#print(part1(lines))
print(part2(lines))