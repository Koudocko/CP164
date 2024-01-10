"""
-------------------------------------------------------
Determine if name is valid in python
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from functions import is_valid

name = "^invalid_name"

valid = is_valid(name)

print(f"is_valid('{name}') -> {valid}")
