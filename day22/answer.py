def part1(p1, p2):
    while p1 != [] and p2 != []:
        if p1[0] > p2[0]:
            p1.append(p1[0])
            p1.append(p2[0])
            p1.pop(0)
            p2.pop(0)
        else:
            p2.append(p2[0])
            p2.append(p1[0])
            p1.pop(0)
            p2.pop(0)

    if p1:
        total = sum([p1[i] * (len(p1) - i) for i in range(len(p1))])
    elif p2:
        total = sum([p2[i] * (len(p2) - i) for i in range(len(p2))])

    return total

def part2(p1, p2):
    
    winner, score = run_game(p1, p2)
    return score

def run_game(p1, p2):
    mem = []
    while p1 != [] and p2 != []:
        state = ",".join([str(num) for num in p1]) + " " + ",".join([str(num) for num in p2])
        if state in mem:
            return "p1", sum([p1[i] * (len(p1) - i) for i in range(len(p1))])
        else:
            p1_draw = p1[0]
            p2_draw = p2[0]
            if len(p1) - 1 >= p1_draw and len(p2) - 1 >= p2_draw:
                winner, score = run_game(p1[1:p1_draw+1], p2[1:p2_draw+1])
                if winner == "p1":
                    p1.append(p1_draw)
                    p1.append(p2_draw)
                    p1.pop(0)
                    p2.pop(0)
                elif winner == "p2":
                    p2.append(p2_draw)
                    p2.append(p1_draw)
                    p1.pop(0)
                    p2.pop(0)
                else:
                    print("error")
            else:
                if p1_draw > p2_draw:
                    p1.append(p1_draw)
                    p1.append(p2_draw)
                    p1.pop(0)
                    p2.pop(0)
                else:
                    p2.append(p2_draw)
                    p2.append(p1_draw)
                    p1.pop(0)
                    p2.pop(0)
            mem.append(state)
    if p1:
        return "p1", sum([p1[i] * (len(p1) - i) for i in range(len(p1))])
    elif p2:
        return "p2", sum([p2[i] * (len(p2) - i) for i in range(len(p2))])



lines = open("input.txt", "r").readlines()

p1 = []
p2 = []
current_player = p1
for line in lines:
    line = line.strip()
    if line == "Player 1:":
        current_player = p1
    elif line == "Player 2:":
        current_player = p2
    else:
        if line.isdigit():
            current_player.append(int(line))

#print(part1(p1, p2))
print(part2(p1, p2))