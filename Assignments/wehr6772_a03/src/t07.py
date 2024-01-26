"""
-------------------------------------------------------
Assignment 3 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from functions import stack_maze

maze = {'Start': ['A'], 'A':['B'], 'B':['A']}
path = stack_maze(maze)

print(f"stack_maze({maze})-> {path}")
