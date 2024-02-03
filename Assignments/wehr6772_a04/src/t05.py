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
from Priority_Queue_array import Priority_Queue
from functions import pq_split_key

source = Priority_Queue()
source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)
source.insert(5)

key = 100

print(f"Key: {key} - Source: ", end="")
for ele in source:
    print(f"{ele}", end=" ")
print()

target1, target2 = pq_split_key(source, key)

print("Target 1: ", end="")
for ele in target1:
    print(f"{ele}", end=" ")
print()

print("Target 2: ", end="")
for ele in target2:
    print(f"{ele}", end=" ")
print()
