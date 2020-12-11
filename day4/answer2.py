f = open("./input.txt", "r")

lines = f.readlines()

def check_doc(cat, val):
    if cat == 'byr':
        if len(val) != 4 or (int(val) < 1920 or int(val) > 2002):
            return False
        else:
            return True
    elif cat == 'iyr':
        if len(val) != 4 or (int(val) < 2010 or int(val) > 2020):
            return False
        else:
            return True
    elif cat == 'eyr':
        if len(val) != 4 or (int(val) < 2020 or int(val) > 2030):
            return False
        else:
            return True
    elif cat == 'hgt':
        if len(val) <= 2:
            return False
        unit = val[len(val) - 2 : len(val)]
        val = val[:len(val) - 2]
        
        if unit != 'cm' and unit != 'in':
            return False
        elif unit == 'cm' and (int(val) < 150 or int(val) > 193):
            return False
        elif unit == 'in' and (int(val) < 59 or int(val) > 76):
            return False
        else:
            return True
    elif cat == 'hcl':
        if val[0] != '#':
            return False
        val = val[1:]
        char_count = 0
        for char in val:
            if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                return False
            else:
                char_count += 1
        if char_count != 6:
            return False
        else:
            return True
    elif cat == 'ecl':
        if val not in ['amb','blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        else:
            return True
    elif cat == 'pid':
        char_count = 0
        for char in val:
            if not char.isdigit():
                return False
            else:
                char_count += 1
        return char_count == 9
    else:
        return True

requirements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
valid_count = 0
document = []
for i in range(len(lines) + 1):
    if i == len(lines) or lines[i] == '\n':
        invalid_data = False
        for doc in document:
            cat = doc[0]
            val = doc[1]
            if not check_doc(cat, val):
                
                invalid_data = True
            if cat in requirements:
                requirements.remove(cat)
        if not invalid_data and (requirements == ['cid'] or requirements == []):
            
            valid_count += 1
        requirements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
        document = []
    else:
        line = lines[i]
        line = line.strip('\n')
        fields = line.split(" ")
        field_names = [[x.split(':')[0], x.split(':')[1]] for x in fields]
        document.extend(field_names)

print(valid_count)