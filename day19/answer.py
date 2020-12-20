import re

def part1(rules, messages):
    count = 0

    def build(r_i):
        if not isinstance(rules[r_i], list):
            return rules[r_i]
        elif len(rules[r_i]) == 1:
            s = ""
            for num in rules[r_i][0]:
                s += build(num)
            return s
        else:
            s = ""
            t = []
            for part in rules[r_i]:
                s = ""
                for num in part:
                    s += build(num)
                t.append(s)
            return "(" + t[0] + "|" + t[1] + ")"
    regext_expr = "^" + build(0) + "$"
    print(regext_expr)
            
    for m in messages:
        if bool(re.match(regext_expr, m)):
            count += 1
        
    return count






input_messages = open("./input_message.txt", "r").readlines()
input_rules = open("./input_rules.txt", "r").readlines()

messages = [m.strip() for m in input_messages]
rules = {}
for r in input_rules:
    r = r.strip()
    rule_index, rule = r.split(": ")[0], r.split(": ")[1]
    if not rule[1].isalpha():
        rule = [[int(num) for num in part.split(" ")] for part in rule.split(" | ")]
    else:
        rule = rule[1]
    rules[int(rule_index)] = rule

print(part1(rules, messages))