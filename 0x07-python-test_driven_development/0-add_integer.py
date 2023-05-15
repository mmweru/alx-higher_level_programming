#!/usr/bin/python3
"""This module adds two integers or floating numbers to return
    an integer number."""


def add_integer(a, b=98):
    """A function that computes the summation of two integers.
    Args:
        a(int): The first argument which is of type integer.
        b(int): The second argument which is an integer.
    Return:
        An integer which is the result of the summation.
    Raises:
        TypeError: If a or b are not integers or floats.
    """

    if not isinstance(a , int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b , int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
