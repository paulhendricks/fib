#!/usr/bin/python3
"""Module for Cython code.

Description.

Available defs:
- cyfibf: Returns the nth Fibonacci number.
"""


def cyfibf(long n):
    """Returns the nth Fibonacci number."""
    cdef long a=0, b=1, i
    for i in range(n):
        a, b = a + b, a
    print("Hello world!")
    return a
