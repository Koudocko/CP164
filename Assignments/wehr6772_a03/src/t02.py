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
source1 = Stack()
source2 = Stack()

array1 = [1, 2, 3]
array2 = []
array_to_stack(source1, deepcopy(array1))
array_to_stack(source2, deepcopy(array2))

source.combine(source1, source2)


print(f".combine({array1}, {array2}) -> ", end='')
for ele in source:
    print(f"{ele} ", end='')
print()
