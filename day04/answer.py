f = open("./input.txt", "r")

lines = f.readlines()

requirements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

invalid_count = 0
document = []
for i in range(len(lines) + 1):
    if i == len(lines) or lines[i] == '\n':
        for doc in document:
            if doc in requirements:
                requirements.remove(doc)
        if requirements == ['cid'] or requirements == []:
            print(requirements)
            invalid_count += 1
        requirements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
        document = []
    else:
        line = lines[i]
        line = line.strip('\n')
        fields = line.split(" ")
        field_names = [x.split(':')[0] for x in fields]
        document.extend(field_names)

print(invalid_count)