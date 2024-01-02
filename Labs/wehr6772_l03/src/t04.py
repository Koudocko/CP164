"""
-------------------------------------------------------
Lab 4 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

import sys,os
sys.path.append(os.path.realpath('../../../login_data_structures/src'))

from Priority_Queue_array import Priority_Queue

q = Priority_Queue()

print("Insert 22")
q.insert(22)
print(f"Peek {q.peek()}")

print("Insert 33")
q.insert(33)
print(f"Peek {q.peek()}")

print("Insert 11")
q.insert(11)
print(f"Peek {q.peek()}")

print("Insert 55")
q.insert(55)
print(f"Peek {q.peek()}")

print("Insert 44")
q.insert(44)
print(f"Peek {q.peek()}")
