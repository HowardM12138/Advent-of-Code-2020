def part1(lines):
    mem = parse_part1(lines)
    for pos in mem:
        decimal = mem[pos][0]
        bit_mask = mem[pos][1]
        mem[pos] = apply_mask(decimal, bit_mask)
    return sum(mem[pos] for pos in mem)

def parse_part1(lines):
    mem = {}
    current_mask = ""
    for line in lines:
        line = line.strip()
        if 'mask' in line:
            current_mask = line.split(" = ")[1]
        else:
            mem[int(line.split('[')[1].split(']')[0])] = [int(line.split(" = ")[1]), current_mask]
    return mem

def apply_mask(decimal, bit_mask):
    bits = bin(decimal).replace("0b", "")
    while len(bits) != 36:
        bits = '0' + bits
    for i in range(len(bit_mask)):
        if bit_mask[i] != "X":
            bits = bits[:i] + bit_mask[i] + bits[i+1:]
    return int(bits, 2)

def part2(lines):
    mem = parse_part2(lines)
    return sum(mem[pos] for pos in mem)

def parse_part2(lines):
    current_mask = ""
    mem = {}
    for line in lines:
        line = line.strip()
        if 'mask' in line:
            current_mask = line.split(" = ")[1]
        else:
            val = int(line.split(" = ")[1])
            pos_lst = get_pos(int(line.split('[')[1].split(']')[0]), current_mask)
            for pos in pos_lst:
                mem[pos] = val
    return mem
            
def get_pos(pos, bit_mask):
    bits = bin(pos).replace("0b", "")
    while len(bits) != 36:
        bits = '0' + bits
    for i in range(len(bit_mask)):
        if bit_mask[i] != '0':
            bits = bits[:i] + bit_mask[i] + bits[i+1:]
    def helper(bits):
        if bits == "":
            return [""]
        else:
            rest = helper(bits[1:])
            if bits[0] == "X":
                rest = rest + rest
                for i in range(len(rest) // 2):
                    rest[i] = '0' + rest[i]
                for j in range(len(rest) // 2, len(rest)):
                    rest[j] = '1' + rest[j]
                return rest
            else:
                for i in range(len(rest)):
                    rest[i] = bits[0] + rest[i]
                return rest
    pos_lst = helper(bits)
    for i in range(len(pos_lst)):
        pos_lst[i] = int(pos_lst[i], 2)
    return pos_lst



f = open("./input.txt", "r")

# print(part1(f.readlines()))
print(part2(f.readlines()))