def part1_process(allergen_dict):
    ingredient_dict = {}

    def process():
        for allergen, ingredient_lst in allergen_dict.items():
            ingredient_set = set(ingredient_lst[0])
            for ingredients in ingredient_lst:
                ingredient_set = ingredient_set.intersection(set(ingredients))
            if len(ingredient_set) == 1:
                ingredient = list(ingredient_set)[0]
                return allergen, ingredient
    
    while len(list(allergen_dict.keys())) != 0:
        
        allergen, ingredient = process()
        allergen_dict.pop(allergen)
        ingredient_dict[ingredient] = allergen
        for allergen, ingredient_lst in allergen_dict.items():
            for ingredients in ingredient_lst:
                if ingredient in ingredients:
                    ingredients.remove(ingredient)
    return ingredient_dict


def part1(allergen_list, all_ingredient):
    count = 0
    check = list(allergen_list.keys())
    for ingredient in all_ingredient:
        if ingredient not in check:
            count += 1
    return count

lines = open("./input.txt", "r").readlines()

allergen_dict = {}
for line in lines:
    line = line.strip()
    args = line.split(" (contains ")
    ingredients = args[0].split(" ")
    allergens = args[1][:-1].split(", ")
    for allergen in allergens:
        if allergen not in list(allergen_dict.keys()):
            allergen_dict[allergen] = []
        allergen_dict[allergen].append(ingredients)

all_ingredient = []
for line in lines:
    line = line.strip()
    args = line.split(" (contains ")
    ingredients = args[0].split(" ")
    all_ingredient.extend(ingredients)

ingredient_dict = part1_process(allergen_dict)

print(part1(ingredient_dict, all_ingredient))

new_dict = {k: v for k, v in sorted(ingredient_dict.items(), key=lambda item: item[1])}

answer = ""
for key in new_dict:
    answer += key + ","
print(answer[:-1])