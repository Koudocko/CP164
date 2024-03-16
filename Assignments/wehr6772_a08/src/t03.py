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

tree = BST()
for char in DATA1:
    tree.insert(Letter(char))

file_variable = open("miserables.txt", "r")
do_comparisons(file_variable, tree)
file_variable.close()

letter_table(tree)
