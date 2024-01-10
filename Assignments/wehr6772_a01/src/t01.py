"""
-------------------------------------------------------
Removes duplicates from list
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from functions import clean_list
from copy import deepcopy

values = [1, 2, 0, 1, 4, 1, 1, 2, 2, 5, 4, 3, 1, 3, 3, 4, 2, 4, 3, 1, 3, 0, 3, 0, 0]
values_copy = deepcopy(values)

clean_list(values)
print(f"clean_list({values_copy}) -> {values}")
