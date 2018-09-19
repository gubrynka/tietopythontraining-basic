'''
Write @access_required decorator that when applied to a function executes
subjected function only if has_access function from authorization.py
returns True. So we can do this:
@access_required
def restricted_print(*args, **kwargs):
print(*args, **kwargs)

restricted_print('1 - visible')
restricted_print('2 - invisible')
restricted_print('3 - invisible')
restricted_print('4 - visible')
'''


from authorization import has_access


def access_required(func):
    def fun_wrapper(*args, **kwargs):
        if has_access():
            func(*args, **kwargs)
    return fun_wrapper


@access_required
def restricted_print(*args, **kwargs):
    print(*args, **kwargs)


if __name__ == "__main__":
    restricted_print('1 - visible')
    restricted_print('2 - invisible')
    restricted_print('3 - invisible')
    restricted_print('4 - visible')
