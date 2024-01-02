"""
-------------------------------------------------------
Lab 3 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

import sys,os
sys.path.append(os.path.realpath('../../../login_data_structures/src'))

from Stack_array import Stack
from utilities import stack_to_array

s = Stack()
for i in range(1, 6):
    s.push(i)

source = []

print(f"Stack top: {s.peek()}")

print(f"List before: {source}")
stack_to_array(s, source)
print(f"List after: {source}")
