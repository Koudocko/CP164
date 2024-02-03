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
from Queue_circular import Queue

q = Queue()

print(f"len(): {len(q)}")
print(f"is_empty(): {q.is_empty()}")
q.insert(1)
q.insert(2)
q.insert(3)
print("insert(1, 2, 3)")

print(f"len(): {len(q)}")
print(f"is_empty(): {q.is_empty()}")
print(f"is_full(): {q.is_full()}")
q.insert(4)
q.insert(5)
q.insert(6)
q.insert(7)
q.insert(8)
q.insert(9)
q.insert(10)
print("insert(4, 5, 6, 7, 8, 9, 10)")
print(f"is_full(): {q.is_full()}")

print(f"len(): {len(q)}")
print(f"remove(): {q.remove()}")
print(f"peek(): {q.peek()}")

print("Queue: ", end="")
for ele in q:
    print(f"{ele}", end=" ")
print()
