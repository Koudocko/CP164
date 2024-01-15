"""
-------------------------------------------------------
Lab 2 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

from Stack_array import Stack
from utilities import array_to_stack

s = Stack()
source = [1, 2, 3, 4, 5]

print(f"List before: {source}")
array_to_stack(s, source)
print(f"List after: {source}")

print(f"Stack top: {s.peek()}")
