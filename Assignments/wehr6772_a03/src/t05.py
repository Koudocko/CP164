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
from functions import is_palindrome_stack

string = "1O2P3O4"
palindrome = is_palindrome_stack(string)

print(f"is_palindrome_stack('{string}') -> {palindrome}")
