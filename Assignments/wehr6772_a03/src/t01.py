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
from functions import stack_combine
from Stack_array import Stack 
from utilities import array_to_stack
from copy import deepcopy

source1 = Stack()
source2 = Stack()

array1 = [5, 8, 12, 8]
array2 = [3, 6, 1, 7, 9, 14]
array_to_stack(source1, deepcopy(array1))
array_to_stack(source2, deepcopy(array2))

source = stack_combine(source1, source2)

print(f"stack_combine({array1}, {array2}) -> ", end='')
for ele in source:
    print(f"{ele} ", end='')
print()
