import re
import sys
from collections import defaultdict
from itertools import permutations

INGREDIENTS = 0
ALLERGENS = 1


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    answer = None
    foods = partlines(input_text)
    all_ingredients = set()
    all_allergens = set()
    allergens_for_ingredients = defaultdict(set)  # Keys ingredients, values allergens

    # Collect all the things
    possible = defaultdict(set)  # Keys allergens, values possible ingredients

    ingredients_without_allergens = set()
    for food in foods:
        all_ingredients |= set(food[INGREDIENTS])
        all_allergens |= set(food[ALLERGENS])
    # Inititally, each allergen could be in any ingredient
    for a in all_allergens:
        possible[a] = all_ingredients.copy()
    # If an allergen is in a food, it must be in one of the ingredients
    for food in foods:
        for a in food[ALLERGENS]:
            possible[a] &= set(food[INGREDIENTS])
    for a in all_allergens:  # For each ingredient, what allergens could it contain
        for i in possible[a]:
            allergens_for_ingredients[i].add(a)
    for i in all_ingredients:  # Which ingredients can't be any allergen
        if not allergens_for_ingredients[i]:
            print(f"{i} cannot contain any allergens")
            ingredients_without_allergens.add(i)

    finished = False
    dangerous = {}
    dangerous2 = {}
    while possible:
        print(f"Possible")
        for a in possible:
            print(f"Allergen {a}, {len(possible[a])}, {possible[a]}")
        allergens_identified = {}
        for allergen in possible:
            if len(possible[allergen]) == 1:
                i = possible[allergen].pop()
                print(f"Id allergen {allergen} is in {i}")
                dangerous[i] = allergen
                dangerous2[allergen] = i
                allergens_identified[allergen] = i
        for allergen, i in allergens_identified.items():
            del possible[allergen]
            for a in possible:
                possible[a].discard(i)
    print(dangerous)
    answer = ""
    for a in sorted(list(all_allergens)):
        answer += dangerous2[a] + ","
    answer = answer[:-1]
    return answer


def partlines(s):
    foods = []
    for line in s.split("\n"):
        line = line.strip()
        ingredients, allergens = line.split("(contains")
        ingredients = ingredients.split()
        allergens = [allergen.strip(",") for allergen in allergens.split()]
        allergens = [allergen.strip(")") for allergen in allergens]

        food = [ingredients, allergens]
        foods.append(food)
    return foods


if __name__ == "__main__":
    exit(main())
