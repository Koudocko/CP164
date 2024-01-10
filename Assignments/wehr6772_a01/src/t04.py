"""
-------------------------------------------------------
Count stats of file
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from functions import file_analyze

fv_0, fv_1 = open("t04.txt", "r"), open("t04.txt", "r")

for line in fv_0:
    print(line)

upp, low, dig, whi, rem = file_analyze(fv_1)

print(f"file_analyze('t04.txt') -> ({upp}, {low}, {dig}, {whi}, {rem})")

fv_0.close()
fv_1.close()
