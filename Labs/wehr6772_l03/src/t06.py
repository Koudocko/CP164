"""
-------------------------------------------------------
Lab 6 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

import sys,os
sys.path.append(os.path.realpath('../../../login_data_structures/src'))
sys.path.append(os.path.realpath('../../../wehr6772_data_structures/src'))

from Priority_Queue_array import Priority_Queue
from Food_utilities import read_foods
from utilities import array_to_queue, queue_to_array, queue_test

fh = open("foods.txt", "r")

pq = Priority_Queue()
values = read_foods(fh)
fh.close()

print("Array to queue")
array_to_queue(pq, values)
print(f"Queue peek: {pq.peek()}")
print(f"List now: {values}")
print()

print("Queue to array")
queue_to_array(pq, values)
print(f"Queue empty: {pq.is_empty()}")
print()

print("Queue test")
queue_test(pq)
