"""
-------------------------------------------------------
Lab 7 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

import sys,os
sys.path.append(os.path.realpath('../../../wehr6772_data_structures/src'))

from Food import Food
from Food_utilities import *

fh = open("foods.txt")

for food in get_vegetarian(read_foods(fh)):
    print(f"{food}\n")
