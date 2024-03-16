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

from BST_linked import BST

x = BST()
x.insert(11)
x.insert(22)
x.insert(33)
x.insert(44)

print(x.one_child_count())
