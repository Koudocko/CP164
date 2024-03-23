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

from functions import *
from Hash_Set_BST import *

fv = open("otoos610.txt", "r")
hash_set = Hash_Set_BST(20)

insert_words(fv, hash_set)
total, max_word = comparison_total(hash_set)

print("Using linked BST Hash_Set")
print(f"Total Comparisons: {total:,}")
print(f"Word with maximum comparisons '{max_word.word}': {max_word.comparisons}")

fv.close()
