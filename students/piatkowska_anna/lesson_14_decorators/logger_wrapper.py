'''
Logger wrapper - write a function called logger_wrapper
that wraps call to any function in order to log passed args.
The function must take foo, *args and **kwargs, prints *args
and **kwargs in human readable format and finally call foo
with args and kwargs
'''


def hello(name, right=True, start=1):
    print("Hello " + name + "!")
    print("right value:", right)
    print("start value:", start)


def logger_wrapper(foo, *args, **kwargs):
    a = '('
    for ar in args:
        a += str(ar)
        a += ", "
    if len(a) > 1:  # "there is already ( character"
        a = a[:-2]
    if len(kwargs.items()) > 0:
        a += ", "
        a += ", ".join(f"{k} = {v}" for k, v in kwargs.items())
    a += ')'
    print("Function will be called:", foo.__name__ + a)
    return foo(*args, **kwargs)


def empty_func():
    pass


if __name__ == "__main__":
    args_list = ["Bob"]
    kwargs_dict = {'right': False, 'start': 2}
    kwargs_print = {'end': "!!!!"}
    logger_wrapper(hello, *args_list, **kwargs_dict)
    logger_wrapper(print, *args_list, **kwargs_print)
    print()
    logger_wrapper(empty_func)
