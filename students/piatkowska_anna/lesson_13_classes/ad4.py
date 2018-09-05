'''
Selective shallow compare - write a function
that for given 2 objects and list
of attribute names checks if objects' attributes are equal.
'''

import ad1


class Student:
    def __init__(self, name, x):
        self.name = name
        self.x = x


def selective_shallow_compare(obj1, obj2, attr_list):
    for item in attr_list:
        try:
            return getattr(obj1, item) == getattr(obj2, item)
        except AttributeError:
            return False


if __name__ == "__main__":
    p1 = ad1.Point(3, 4)
    p2 = ad1.Point(4, 4)
    print(selective_shallow_compare(p1, p2, ['x', 'y']))
    print(selective_shallow_compare(p1, p2, ['y']))
    c1 = ad1.Circle(p1, 2)
    c2 = ad1.Circle(ad1.Point(3, 4), 2)
    print(selective_shallow_compare(c1, c2, ['center', 'radius']))
    print(selective_shallow_compare(c1, c2, ['radius']))
    s1 = Student("Jan Kowalski", 3)
    print(selective_shallow_compare(p1, s1, ['name', 'x']))
    print(selective_shallow_compare(p1, s1, ['x']))
