"""
-------------------------------------------------------
Assignment 3 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from functions import postfix

string = "5 4 3 2 1 + + + +"
answer = postfix(string)

print(f"postfix('{string}') -> {answer}")
