"""
-------------------------------------------------------
Lab 7 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

from morse import *
from BST_linked import *

x = BST()

fill_letter_bst(x, DATA1)
print(encode_morse(x, "joe"))
