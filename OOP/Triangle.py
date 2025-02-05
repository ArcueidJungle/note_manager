class Triangle:

    def __init__(self, a, b, c):
        self.from_sides(a, b, c)
        self.__a = a
        self.__b = b
        self.__c = c

    @classmethod
    def from_sides(cls, a, b, c):
        if not (a + b > c) and (a + c > b)  and (b + c > a):
            raise ValueError("Недопустимые стороны")
        else:
            return  cls(a, b, c)