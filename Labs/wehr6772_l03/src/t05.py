"""
-------------------------------------------------------
Lab 3 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

from Priority_Queue_array import Priority_Queue

q = Priority_Queue()

print("Insert 22")
q.insert(22)
print("Insert 11")
q.insert(11)
print(f"Peek {q.peek()}")

print("Remove first")
q.remove()
print(f"Peek {q.peek()}")
