'''
Exercise 1
Write a definition for a class named Circle with attributes
center and radius, where center is a Point object and radius is a number.

Instantiate a Circle object that represents a circle with its center at
(150, 100) and radius 75.

Write a function named point_in_circle that takes a Circle and a
Point and returns True if the Point lies in or on the boundary of the circle.

Write a function named rect_in_circle that takes a Circle and a Rectangle
and returns True if the Rectangle lies entirely in or on the boundary of
the circle.

Write a function named rect_circle_overlap that takes a Circle and a
Rectangle and returns True if any of the corners of the Rectangle fall
inside the circle. Or as a more challenging version, return True if any
part of the Rectangle falls inside the circle.
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)


class Rectangle:
    def __init__(self, point, width, height):
        self.corner = point
        self.width = width
        self.height = height


class Circle:
    def __init__(self, point, radius):
        self.center = point
        self.radius = radius


def point_in_circle(circle, point):
    return (
        (point.x - circle.center.x)**2 +
        (point.y - circle.center.y)**2) <= circle.radius ** 2


def rect_in_circle(circle, rect):
    return (point_in_circle(circle, rect.corner) and
            point_in_circle(circle,
                            Point(
                                rect.corner.x + rect.width,
                                rect.corner.y)) and
            point_in_circle(circle,
                            Point(rect.corner.x + rect.width,
                                  rect.corner.y + rect.height)) and
            point_in_circle(circle,
                            Point(rect.corner.x, rect.corner.y + rect.height)))


def point_in_rectangle(point, rect):
    return ((rect.corner.x <= point.x and
             rect.corner.x + rect.width >= point.x)
            and (rect.corner.y <= point.y and
                 rect.corner.y + rect.height >= point.y))


def line_intersect_circle(point_a, point_b, circle):
    dx = point_b.x - point_a.x
    dy = point_b.y - point_a.y
    D = point_a.x * point_b.y - point_b.x * point_a.y
    return(circle.radius ** 2 * (dx**2 + dy**2)) >= D**2


def rect_circle_overlap(circle, rect):
    return (point_in_rectangle(circle.center, rect) or
            line_intersect_circle(
                rect.corner,
                Point(rect.corner.x + rect.width, rect.corner.y), circle) or
            line_intersect_circle(
                rect.corner,
                Point(rect.corner.x, rect.corner.y + rect.height), circle) or
            line_intersect_circle(
            Point(rect.corner.x + rect.width, rect.corner.y),
            Point(rect.corner.x + rect.width, rect.corner.y + rect.height),
            circle) or
            line_intersect_circle(
            Point(rect.corner.x, rect.corner.y + rect.height),
            Point(rect.corner.x + rect.width, rect.corner.y + rect.height),
            circle))


if __name__ == "__main__":
    center = Point(150, 100)
    circle = Circle(center, 75)
    print("For circle with center", circle.center, "and radius 75")
    print("Point in circle:")
    print("(160, 120): ", point_in_circle(circle, Point(160, 120)))
    print("(70, 120): ", point_in_circle(circle, Point(70, 120)))
    print("(75, 100): ", point_in_circle(circle, Point(75, 100)))

    print("For rectangle with bottom left corner in (", center.x, ",", center.y, ")\
    and width: 10 and height 10")
    rect = Rectangle(center, 10, 10)
    print("Rect in circle: ", rect_in_circle(circle, rect))
    print("Rect and circle overlap: ", rect_circle_overlap(circle, rect))
    print("For rectangle with bottom left corner in (", center.x, ",", center.y, ")\
    and width: 100 and height 100")
    rect = Rectangle(center, 100, 100)
    print("Rect in circle: ", rect_in_circle(circle, rect))
    print("Rect and circle overlap: ", rect_circle_overlap(circle, rect))

    print("For rectangle with bottom left corner in (", center.x - 100, ",", center.y - 100, ")\
    and width: 200 and height 200")
    new_center = Point(center.x - 100, center.y - 100)
    rect = Rectangle(new_center, 200, 200)
    print("Rect in circle: ", rect_in_circle(circle, rect))
    print("Rect and circle overlap: ", rect_circle_overlap(circle, rect))

    print("For rectangle with bottom left corner in (", 100, ",", 0, ")\
    and width: 100 and height 50")
    new_center = Point(100, 0)
    rect = Rectangle(new_center, 100, 50)
    print("Rect in circle: ", rect_in_circle(circle, rect))
    print("Rect and circle overlap: ", rect_circle_overlap(circle, rect))
