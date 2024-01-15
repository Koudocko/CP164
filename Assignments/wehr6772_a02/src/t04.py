"""
-------------------------------------------------------
Assignment 1 Testing
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

food_table(foods)

fh.close()
