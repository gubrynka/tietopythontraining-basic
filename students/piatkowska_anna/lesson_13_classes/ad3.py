'''
Object inspector 2 - write a function that for a given
object returns dictionary with names and values of all
object's attributes that are instances of string, integer or float.
'''
import ad1


class Worker:
    def __init__(self, name, age, salary, friends):
        self.name = name
        self.age = age
        self.salary = salary
        self.friend = friends


def inspect_object(object):
    result = {}
    attributes = vars(object)
    for item in attributes:
        if isinstance(getattr(object, item), (str, int, float)):
            result[item] = getattr(object, item)
    return result


if __name__ == "__main__":
    p = ad1.Point(3, 3)
    print(inspect_object(p))
    w = Worker("John Doe", 20, 2.23, ["ala", "ola", "ela"])
    print(inspect_object(w))
