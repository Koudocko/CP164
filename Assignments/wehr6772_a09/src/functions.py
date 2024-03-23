"""
-------------------------------------------------------
Assignment 9 functions
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

from Word import *

def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a Hash_Set. Each Word object in hash_set contains the number
    of comparisons required to insert that Word object from
    file_variable into hash_set.
    Use: insert_words(file_variable, hash_set)
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """

    line = fv.readline()

    while line != "":
        for word in line.split():
            if word.isalpha():
                hash_set.insert(Word(word.lower())) 

        line = fv.readline()

    return

def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    Use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """

    total = 0
    max_word = None

    for word in hash_set:
        if max_word is None:
            max_word = word
        elif word.comparisons > max_word.comparisons:
            max_word = word

        total += word.comparisons

    return (total, max_word)