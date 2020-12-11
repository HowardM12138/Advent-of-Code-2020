f = open("./input.txt", "r")

numbers = f.readlines()

count = 0
for i in range(len(numbers)):
    args = numbers[i].split(' ')
    min = int(args[0].split('-')[0])
    max = int(args[0].split('-')[1])
    letter = args[1][0]
    password = args[2]
    password = password.strip('\n')

    # print(min, max, letter, password)

    char_count = 0
    for j in range(len(password)):
        if password[j] == letter:
            char_count += 1

    if char_count >= min and char_count <= max:
        count += 1

print(count)