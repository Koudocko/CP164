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

# Imports
from BST_linked import BST
from Letter import Letter
from functions import *

# Constants
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"


tree1 = BST()
for char in DATA1:
    tree1.insert(Letter(char))

file_variable = open("miserables.txt", "r")
do_comparisons(file_variable, tree1)
file_variable.close()

tree2 = BST()
for char in DATA2:
    tree2.insert(Letter(char))

file_variable = open("miserables.txt", "r")
do_comparisons(file_variable, tree2)
file_variable.close()

tree3 = BST()
for char in DATA3:
    tree3.insert(Letter(char))

file_variable = open("miserables.txt", "r")
do_comparisons(file_variable, tree3)
file_variable.close()

print(f"Comparing by order: {DATA1}")
print(f"Total Comparisons: {comparison_total(tree1)}")

print(f"Comparing by order: {DATA2}")
print(f"Total Comparisons: {comparison_total(tree2)}")

print(f"Comparing by order: {DATA3}")
print(f"Total Comparisons: {comparison_total(tree3)}")
