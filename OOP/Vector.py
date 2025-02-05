from math import sqrt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    @property
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)

v1 = Vector(2, 3)
v2 = Vector(5, 7)
v3 = v1 + v2
print(v3)                 # Vector(7, 10)
print(v3.magnitude)       # ≈ 12.2065
print(v1 == Vector(2, 3)) # True
print(v1 - v2)            # Vector(-3, -4)