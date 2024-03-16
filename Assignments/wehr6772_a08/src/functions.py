"""
-------------------------------------------------------
Assignment 8 functions
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from BST_linked import BST
from Letter import Letter

def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0

    # your code here
    line = file_variable.readline()

    while line != "":
        for char in line:
            if char.isalpha():
                bst.retrieve(Letter(char.upper()))

        line = file_variable.readline()


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """

    elements = bst.inorder()
    total = 0

    for char in elements:
        total += char.comparisons

    return total



def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """

    elements = bst.inorder()
    total = 0

    for char in elements:
        total += char.count

    print("Letter Count/Percent Table")
    print()

    print(f"Total Count: {total:,}")
    print()

    print("Letter  Count       %")
    print("---------------------")

    for char in elements:
        percent = char.count / total * 100
        print(f"{char.letter:>5s}{char.count:>8,d}{percent:7.2f}%")

    return
