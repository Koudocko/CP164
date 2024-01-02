"""
-------------------------------------------------------
Lab 5 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

import sys,os
sys.path.append(os.path.realpath('../../../login_data_structures/src'))
sys.path.append(os.path.realpath('../../../wehr6772_data_structures/src'))

from utilities import stack_test
from Food_utilities import read_foods

fh = open("foods.txt", "r")

stack_test(read_foods(fh))
