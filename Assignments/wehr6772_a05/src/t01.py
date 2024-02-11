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
from List_array import List

list1 = List()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(2)
list1.append(1)

print("List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

list2 = List()
list2.append(1)
list2.append(2)
list2.append(3)
list2.append(2)
list2.append(1)

print("List 2 contents:")
for val in list2:
    print(val, end=" ")
print("\n")

print(f"List 1 == list 2: {list1 == list2}\n")

print(f"List 1 item at idx 2: {list1[2]}\n")

list1.append(100)
print("list1.append(100)\n")

print("List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print(f"List 1 == list 2: {list1 == list2}\n")

print("list1.clean()\n")
list1.clean()

print("List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

list3 = List()
list3.append(50)
list3.append(50)
list3.append(50)
list3.append(50)
list3.append(50)

print("List 3 contents:")
for val in list3:
    print(val, end=" ")
print("\n")

list4 = List()
list4.append(-50)
list4.append(-50)
list4.append(-50)
list4.append(-50)
list4.append(-50)

print("List 4 contents:")
for val in list4:
    print(val, end=" ")
print("\n")

print("list1.combine(list3, list4)\n")
list1.combine(list3, list4)

print("List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list3.append(1000)")
list3.append(1000)

print("list4.append(1000)\n")
list4.append(1000)

print("list1.intersection(list3, list4)\n")
list1.intersection(list3, list4)

print("List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list1.prepend(1000)\n")
list1.prepend(1000)

print("List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list1.remove_front()\n")
list1.remove_front()

print("List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list1.remove_front(50)")
list1.remove_many(50)

print("list1.remove_front(-50)\n")
list1.remove_many(-50)

print("List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list5, list6 = list1.split()")
list5, list6 = list1.split()

print("List 5 contents:")
for val in list5:
    print(val, end=" ")
print("\n")

print("List 6 contents:")
for val in list6:
    print(val, end=" ")
print("\n")

print("List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list1.insert(1) x3")
print("list1.insert(0) x3\n")
list1.append(1)
list1.append(0)
list1.append(1)
list1.append(0)
list1.append(1)
list1.append(0)

print("List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list5, list6 = list1.split_alt()")
list7, list8 = list1.split_alt()

print("List 7 contents:")
for val in list7:
    print(val, end=" ")
print("\n")

print("List 8 contents:")
for val in list8:
    print(val, end=" ")
print("\n")

print("List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")

print("list1.union(list7, list8)\n")
list1.union(list7, list8)

print("List 1 contents:")
for val in list1:
    print(val, end=" ")
print("\n")
