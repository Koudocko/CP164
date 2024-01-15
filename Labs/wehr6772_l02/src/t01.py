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

from Stack_array import Stack

s = Stack()
print(f"Empty: {s.is_empty()}")

s.push(1)
print("Pushed 1")

print(f"Empty: {s.is_empty()}")

s.push(2)
print("Pushed 2")

print(f"Top: {s.peek()}")
print(f"Popped: {s.pop()}")
print(f"Top: {s.peek()}")
