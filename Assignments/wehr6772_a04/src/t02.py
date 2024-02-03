"""
-------------------------------------------------------
Assignment 4 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from Queue_array import Queue

q1 = Queue()
q1.insert(1)
q1.insert(2)
q1.insert(3)

q2 = Queue()
q2.insert(1)
q2.insert(2)
q2.insert(3)
q2.insert(4)

print("Queue 1: ", end="")
for ele in q1:
    print(f"{ele}", end=" ")
print()

print("Queue 2: ", end="")
for ele in q2:
    print(f"{ele}", end=" ")
print()

print(f"Queue 1 == Queue2: {q1 == q2}")
