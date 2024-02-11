"""
-------------------------------------------------------
Assignment 5 Testing
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from Sorted_List_array import Sorted_List

list1 = Sorted_List()
list1.insert(1)
list1.insert(2)
list1.insert(3)
list1.insert(2)
list1.insert(1)

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print(f"Sorted_List 1 contains 3: {3 in list1}")
print(f"Sorted_List 1 contains 100: {100 in list1}\n")

list2 = Sorted_List()
list2.insert(1)
list2.insert(2)
list2.insert(3)
list2.insert(2)
list2.insert(1)

print("Sorted_List 2 contents:")
for val in list2:
    print(val, end=" ")
print("\n")

print(f"Sorted_List 1 == list 2: {list1 == list2}\n")

print(f"Sorted_List 1 item at idx 2: {list1[2]}\n")

list1.insert(100)
print("list1.insert(100)\n")

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print(f"Sorted_List 1 == list 2: {list1 == list2}\n")

print("list1.clean()\n")
list1.clean()

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print(f"list1.count(100): {list1.count(100)}\n")

print("list1.insert(100)\n")
list1.insert(100)

print(f"list1.count(100): {list1.count(100)}\n")

print(f"list1.find(100): {list1.find(100)}\n")

print(f"list1.find(100): {list1.find(1000)}\n")

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print(f"list1.index(100): {list1.index(100)}\n")

list3 = Sorted_List()
list3.insert(50)
list3.insert(50)
list3.insert(50)
list3.insert(50)
list3.insert(50)
list3.insert(-100)

print("Sorted_List 3 contents:")
for val in list3:
    print(val, end=" ")
print("\n")

list4 = Sorted_List()
list4.insert(-50)
list4.insert(-50)
list4.insert(-50)
list4.insert(-50)
list4.insert(-50)
list4.insert(-100)

print("Sorted_List 4 contents:")
for val in list4:
    print(val, end=" ")
print("\n")

print("list1.intersection(list3, list4)\n")
list1.intersection(list3, list4)

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print(f"list1.max(): {list1.max()}\n")

print(f"list1.min(): {list1.min()}\n")

print(f"list1.peek(): {list1.peek()}\n")

print(f"list1.remove(100): {list1.remove(100)}\n")

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print(f"list1.remove(1000): {list1.remove(1000)}\n")

print(f"list1.remove_front(): {list1.remove_front()}\n")

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list1.insert(0) x5\n")
list1.insert(0)
list1.insert(0)
list1.insert(0)
list1.insert(0)
list1.insert(0)

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list1.remove_many(50)")
list1.remove_many(0)

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list5, list6 = list1.split()")
list5, list6 = list1.split()

print("Sorted_List 5 contents:")
for val in list5:
    print(val, end=" ")
print("\n")

print("Sorted_List 6 contents:")
for val in list6:
    print(val, end=" ")
print("\n")

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list1.insert(1) x3")
print("list1.insert(0) x3\n")
list1.insert(1)
list1.insert(0)
list1.insert(1)
list1.insert(0)
list1.insert(1)
list1.insert(0)

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list7, list8 = list1.split_alt()")
list7, list8 = list1.split_alt()

print("Sorted_List 7 contents:")
for val in list7:
    print(val, end=" ")
print("\n")

print("Sorted_List 8 contents:")
for val in list8:
    print(val, end=" ")
print("\n")

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("Updated list1 with elements\n")
list1.insert(1)
list1.insert(27)
list1.insert(5)
list1.insert(100)
list1.insert(4)
list1.insert(3)
list1.insert(1)
list1.insert(2)

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list9, list10 = list1.split_key(7)")
list9, list10 = list1.split_key(5)

print("Sorted_List 9 contents:")
for val in list9:
    print(val, end=" ")
print("\n")

print("Sorted_List 10 contents:")
for val in list10:
    print(val, end=" ")
print("\n")

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list1.union(list9, list10)\n")
list1.union(list9, list10)

print("Sorted_List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")
