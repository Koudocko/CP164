"""
-------------------------------------------------------
Removes contents of subtrahend list from minuend
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from functions import list_subtraction
from copy import deepcopy

minuend = [0, 0, 1, 0, 0, 1, 0, 0]
subtraend = []
minuend_copy = deepcopy(minuend)

list_subtraction(minuend, subtraend)
print(f"list_subtraction({minuend_copy}, {subtraend}) -> {minuend}")
