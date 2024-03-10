"""
-------------------------------------------------------
Lab 9 functions
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
     695    2 Lasagna, 7
    1355    4 Butter Chicken, 2
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """

    print("""
Hashes
Hash     Slot Key
-------- ---- --------------------
          """)

    for val in values:
        val_hash = hash(val)
        val_slot = val_hash % slots

        print(f"{val_hash:>8}{val_slot:>5} {val}")

    return
