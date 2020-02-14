#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Janell.Huyck, using Kenzie's framework of empty funtions"
"""reference: https: // www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/"""


def my_abs(number):
    if number >= 0:
        return number
    else:
        return 0-number


def add(x, y):
    """Add two integers. Handles negative values."""

    return (x + y)


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    result = 0
    for num in range(my_abs(y)):
        result = add(result, my_abs(x))
    if (x >= 0 and y >= 0) or (x <= 0 and y <= 0):
        return result
    else:
        return 0 - result


def power(x, n):
    """Raise x to power n, where n >= 0"""
    result = 1
    for num in range(n):
        result = multiply(result, x)
    return result


def factorial(x):
    """Compute factorial of x, where x > 0"""
    result = 1
    for number in range(1, x+1):
        result = multiply(result, number)
    return result


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
    return b


if __name__ == '__main__':
    # your code to call functions above
    """It doesn't make sense to have anything in this section for these katas
    since they're being called from the testing functions"""

    pass
