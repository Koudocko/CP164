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

from Queue_array import Queue
from utilities import array_to_queue, queue_to_array, queue_test

q = Queue()
values = [1, 2, 3, 4, 5]
print(f"List initial: {values}")
print()

print("Array to queue")
array_to_queue(q, values)
print(f"Queue peek: {q.peek()}")
print(f"List now: {values}")
print()

print("Queue to array")
queue_to_array(q, values)
print(f"Queue empty: {q.is_empty()}")
print(f"List now: {values}")
print()

print("Queue test")
queue_test(q)
