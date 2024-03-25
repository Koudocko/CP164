"""
-------------------------------------------------------
Assignment 10 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

from Sorts_List_linked import *
from List_linked import *
from random import randint

x = List()
for _ in range(0, 100):
    x.append(randint(0, 1000))

Sorts.radix_sort(x)
print("Radix Sort Linked:")

valid = True
last = None

for ele in x:
    print(f"{ele} > ", end="")

    if last is not None:
        if last > ele:
            valid = False

    last = ele

print(f"Is sorted = {valid}")
