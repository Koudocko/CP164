"""
-------------------------------------------------------
Assignment 2 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from Food import Food
from Food_utilities import *

fh = open("foods.txt", "r")

foods = read_foods(fh)
origin = 2
max_cals = 400 
is_veg = False
foods = food_search(foods, origin, max_cals, is_veg)

print(f"ORIGIN: {Food.ORIGIN[origin]}, max calories: {max_cals}, vegetarian: {is_veg}")
for food in foods:
    print(food)

fh.close()
