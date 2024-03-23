"""
-------------------------------------------------------
Assignment 9 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from BST_linked import BST

bst = BST()

bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(5)
bst.insert(0)

one, two, three = bst.node_counts()

print(f"{one} : {two} : {three}")

print(f"4 in bst: {4 in bst}")
print(f"7 in bst: {7 in bst}")

val = bst.parent(3)
val_r = bst.parent_r(3)

print(f"3 - val: {val}, val_r: {val_r}")
