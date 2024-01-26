"""
-------------------------------------------------------
Assignment 3 functions
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2024-01-01"
-------------------------------------------------------
"""

# Imports
from Stack_array import Stack 
from utilities import array_to_stack, stack_to_array
from copy import deepcopy

# Constants
OPERATORS = "+-*/"

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """

    target = Stack()

    while not source1.is_empty() or not source2.is_empty():
        if not source1.is_empty():
            target.push(source1.pop())
        if not source2.is_empty():
            target.push(source2.pop())

    return target

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """

    copy_list = []

    while not source.is_empty():
        copy_list.append(source.pop())

    for ele in copy_list:
        source.push(ele)

    return

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """

    s = Stack()
    filtered_string = ""

    for char in string:
        if char.isalpha():
            filtered_string += char

    for idx in range(0, (len(filtered_string) // 2) - int(len(filtered_string) % 2 == 0) + 1):
        s.push(filtered_string[idx])

    palindrome = True
    for idx in range(len(filtered_string) // 2, len(filtered_string)):
        if filtered_string[idx].lower() != s.pop().lower():
            palindrome = False
            break

    return palindrome

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """

    operations = Stack()

    for op in string.split():
        operations.push(op)

        top = operations.peek()
        if top in OPERATORS:
            operations.pop()
            second = int(operations.pop())
            first = int(operations.pop())

            if top == "+":
                operations.push(first + second)
            elif top == "-":
                operations.push(first - second)
            elif top == "*":
                operations.push(first * second)
            elif top == "/":
                operations.push(first / second)

    answer = operations.pop()
    return answer

def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """

    s = Stack()
    copy_maze = deepcopy(maze)
    array_to_stack(s, copy_maze['Start'])

    while not s.is_empty() and 'X' != s.peek():
        if len(copy_maze[s.peek()]) > 0:
            s.push(copy_maze[s.peek()].pop())
        else:
            s.pop()

    path = []
    stack_to_array(s, path)

    return None if len(path) == 0 else path
