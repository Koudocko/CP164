"""
-------------------------------------------------------
Gets stats of 2d matrix
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from functions import matrix_stats

a = [[36, 15], [24, 72], [64, 19]]

small, total, large, average = matrix_stats(a)

print(f"matrix_stats({a}) -> ({small}, {total}, {large}, {average})")
