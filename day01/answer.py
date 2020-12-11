f = open("input.txt", "r")

numbers = f.readlines()
for i in range(0, len(numbers)-2):
    num1 = int(numbers[i][:-1])
    for j in range(i+1, len(numbers)-1):
        num2 = int(numbers[j][:-1])
        for k in range(j+1, len(numbers)):
            num3 = int(numbers[k][:-1])
            if num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)