#!/usr/bin/python3
"""Module for Cython code.

Description.

Available defs:
- cyfibf: Returns the nth Fibonacci number.
"""

from .cyfib import cyfibf


__all__ = ['pyfibf', 'hello_world', 'wrapper']


def pyfibf():
    """Returns the nth Fibonacci number."""
    print("Hello world! This is pyfib()")


def hello_world():
    """Returns the nth Fibonacci number."""
    print("Hello world!")


def wrapper(n):
    """Returns the nth Fibonacci number."""
    print("This is a wrapper")
    return cyfibf(n)
