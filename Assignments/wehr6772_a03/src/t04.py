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
from Stack_array import Stack 
from utilities import array_to_stack
from copy import deepcopy

source = Stack()
array = [1]

array_to_stack(source, deepcopy(array))
source.reverse()

print(f"stack_reverse({array}) -> ", end='')
for ele in source:
    print(f"{ele} ", end='')
print()
