"""
-------------------------------------------------------
Assignment 6 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

from Sorted_List_linked import Sorted_List

x = Sorted_List()
a, b = Sorted_List(), Sorted_List()
a.insert(99)
a.insert(99)
a.insert(99)
a.insert(99)
b.insert(99)
b.insert(99)
b.insert(99)
b.insert(99)

x.intersection(a, b)

print("x > ", end='')
for ele in x:
    print(f"{ele} > ", end='')
print(x._rear._next)
