'''
Write @sort decorator that when applied to a
function that returns a list, sorts this list, so we can do this:
@sort
def data_feeder():
  return [4,2,1,3]

data_feeder() == [1,2,3,4] # <- this is True
'''


def sort(func):
    def func_wrapper():
        li = func()
        li.sort()
        return li
    return func_wrapper


@sort
def data_feeder():
    return [4, 2, 1, 3]


if __name__ == "__main__":
    print(data_feeder())
