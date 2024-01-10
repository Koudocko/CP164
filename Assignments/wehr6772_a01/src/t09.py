"""
-------------------------------------------------------
Adds two matrices of the same size together
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from functions import matrixes_add

a = [[61, 14], [37, 48], [73, 50]]
b = [[63, 1], [84, 59], [98, 77]]

c = matrixes_add(a, b)

print(f"matrices_add({a}, {b}) -> {c}")
