'''
Object inspector 1 - write a function that for a given object
and list of attribute names returns dictionary with
names and values of object's attributes.
'''
import ad1


def inspect_object(object, list):
    result = {}
    attributes = vars(object)
    for item in list:
        if item in attributes:
            result[item] = getattr(object, item)
    return result


if __name__ == "__main__":
    p = ad1.Point(3, 3)
    print(inspect_object(p, ['x', 'y']))
    print(inspect_object(p, ['y']))
