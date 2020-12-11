f = open("./input.txt", "r")

numbers = f.readlines()

count = 0
for i in range(len(numbers)):
    args = numbers[i].split(' ')
    pos1 = int(args[0].split('-')[0]) - 1
    pos2 = int(args[0].split('-')[1]) - 1
    letter = args[1][0]
    password = args[2]
    password = password.strip('\n')

    print(pos1, pos2, letter, password)

    char_count = 0
    if password[pos1] == letter:
        char_count += 1
    if password[pos2] == letter:
        char_count += 1

    print(char_count)
    if char_count == 1:
        count += 1

print(count)