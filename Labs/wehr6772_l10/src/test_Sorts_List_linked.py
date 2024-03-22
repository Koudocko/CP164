"""
-------------------------------------------------------
Tests various linked sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2019-04-27"
-------------------------------------------------------
"""
# Imports
import random

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()

    for num in range(SIZE):
        values.append(Number(num))

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()

    for num in range(SIZE - 1, -1, -1):
        values.append(Number(num))

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """

    # your code here
    lists = List()

    for _ in range(SIZE):
        test = List()

        for _ in range(TESTS):
            test.append(Number(random.randint(0, XRANGE)))

        lists.append(test)

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    Number.comparisons = 0
    Sorts.swaps = 0

    list_s = create_sorted()
    list_r = create_reversed()
    list_rand = create_randoms()

    func(list_s)
    comps_s = Number.comparisons
    swaps_s = round(Sorts.swaps, 0)

    Number.comparisons = 0
    Sorts.swaps = 0

    func(list_r)
    comps_r = Number.comparisons
    swaps_r = round(Sorts.swaps, 0)

    Number.comparisons = 0
    Sorts.swaps = 0

    for test in list_rand:
        func(test)

    comps_rand = Number.comparisons // TESTS
    swaps_rand = Sorts.swaps // TESTS
    Number.comparisons = 0
    Sorts.swaps = 0

    print(f"{title:14} {comps_s:8} {comps_r:8} {comps_rand:8} {swaps_s:8} {swaps_r:8} {swaps_rand:8}")

    return
