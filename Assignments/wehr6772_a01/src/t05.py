"""
-------------------------------------------------------
Determines if year is a leap year
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from functions import is_leap_year

year = 1700

leap_year = is_leap_year(year)

print(f"is_leap_year({year}) -> {leap_year}")
