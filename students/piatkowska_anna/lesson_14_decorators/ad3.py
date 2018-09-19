'''
Write @logged decorator using logger_wrapper from lesson 6.
Apply it to several functions to demonstrate that it works.
'''


import logger_wrapper as lw
from functools import wraps


def logged(func):
    # @wraps(func)
    def func_wrapper(*args, **kwargs):
        return lw.logger_wrapper(func, *args, **kwargs)
    return func_wrapper


@logged
def sum(x, y):
    try:
        return x + y
    except Exception as e:
        print("Error occurred:", str(e))


@logged
def print_hello(name):
    print("Hello", name)


if __name__ == "__main__":
    print(sum('a', 'b'))
    print_hello('Bob')
    print_hello(3)
    print(sum(2, 3))
    print(sum(2, 'b'))
    print(sum('c', 7))
