"""
-------------------------------------------------------
Lab 6 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

from Food import Food
from Food_utilities import *

fh_old, fh_new = open("foods.txt", "r"), open("new_foods.txt", "w")

write_foods(fh_new, read_foods(fh_old))

fh_old.close()
fh_new.close()
