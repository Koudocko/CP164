"""
-------------------------------------------------------
Lab 1 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

import sys,os
sys.path.append(os.path.realpath('../../../login_data_structures/src'))

from Queue_array import Queue

q = Queue()
print(f"Empty: {q.is_empty()}")

print(f"Insert 0")
q.insert(0)
print(f"Empty: {q.is_empty()}")
