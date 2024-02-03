"""
-------------------------------------------------------
Assignment 4 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from Queue_array import Queue

source = Queue()

print("Source: ", end="")
for ele in source:
    print(f"{ele}", end=" ")
print()

target1, target2 = source.split_alt()

print("Target 1: ", end="")
for ele in target1:
    print(f"{ele}", end=" ")
print()

print("Target 2: ", end="")
for ele in target2:
    print(f"{ele}", end=" ")
print()
