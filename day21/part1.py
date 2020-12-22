import re
import sys
from collections import defaultdict
from itertools import permutations


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
    allergens_for_ingredients = defaultdict(set)

    possible = defaultdict(set)
    ingredients_without_allergens = set()
    for food in foods:
        all_ingredients |= set(food[0])
        all_allergens |= set(food[1])
    for a in all_allergens:  # Inititally, each allergen could be in any ingredient
        possible[a] = all_ingredients.copy()
    for food in foods:
        for a in food[
            1
        ]:  # If an allergen is in a food, it must be in one of the ingredients
            possible[a] &= set(food[0])
    for a in all_allergens:  # For each ingredient, what allergens could it contain
        for i in possible[a]:
            allergens_for_ingredients[i].add(a)
    for i in all_ingredients:  # Which ingredients can't be any allergen
        if not allergens_for_ingredients[i]:
            print(f"{i} cannot contain any allergens")
            ingredients_without_allergens.add(i)
    answer = 0
    for i in ingredients_without_allergens:
        for f in foods:
            if i in f[0]:
                answer += 1
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
