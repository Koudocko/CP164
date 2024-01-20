"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

from Food import Food
from copy import deepcopy

def get_food():
    """
    -------------------------------------------------------
    Creates a Food object by requesting data from a user.
    Use: source = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    # Your code here
    name = input("Name: ")

    print("Origin")
    print(Food.origins())
    origin = int(input(": "))

    is_vegetarian = input("Vegetarian (Y/N): ").upper() == 'Y'

    calories = int(input("Calories: "))

    food = Food(name, origin, is_vegetarian, calories)

    return food

def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a Food object from a line of string data.
    Use: source = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """

    # Your code here
    name, origin, is_vegetarian, calories = line.split('|')
    food = Food(name, int(origin), is_vegetarian == "True", int(calories))

    return food

def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """

    # Your code here
    line = file_variable.readline()
    foods = []

    while line != "":
        foods.append(read_food(line))
        line = file_variable.readline()

    return foods

def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of Food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file variable)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here
    for food in foods:
        file_variable.write(
            format(f"{food.name}|{food.origin}|"
                   f"{food.is_vegetarian}|{food.calories}\n"))

    return

def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian Food objects.
    foods is unchanged.
    Use: v_foods = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """

    # Your code here
    veggies = []

    for food in foods:
        if food.is_vegetarian:
            veggies.append(food)

    return veggies

def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of Food objects by origin.
    foods is unchanged.
    Use: o_foods = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    # Your code here
    origins = []

    for food in foods:
        if food.origin == origin:
            origins.append(food)

    return origins

def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """

    # Your code here
    avg = 0

    for food in foods:
        avg += food.calories
    avg /= len(foods)

    return avg

def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: by_origin = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    # Your code here
    avg = average_calories(by_origin(foods, origin))

    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of Food objects, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here
    foods_copy = deepcopy(foods)
    foods_copy.sort()

    print("Food                                Origin       Vegetarian Calories")
    print("----------------------------------- ------------ ---------- --------")

    for food in foods_copy:
        veg_offset = 23 - len(Food.ORIGIN[food.origin])
        print(f"{food.name:<36s}{Food.ORIGIN[food.origin]}{str(food.is_vegetarian):>{veg_offset}}{food.calories:>9}")

    return

def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for Food objects that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    # Your code here
    result = []

    for food in foods:
        if food.origin == -1 or food.origin == origin:
            if max_cals == 0 or food.calories <= max_cals:
                if not is_veg or food.is_vegetarian == is_veg:
                    result.append(food)

    return result
