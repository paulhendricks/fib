from .cyfib import cyfibf


__all__ = ['pyfibf', 'hello_world', 'wrapper']


def pyfibf():
    print("Hello world! This is pyfib()")


def hello_world():
    print("Hello world!")


def wrapper(n):
    print("This is a wrapper")
    return cyfibf(n)
