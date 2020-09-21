from math import sin, cos, acos


class Vec:
    x = 0.0
    y = 0.0

    def __init__(self, x, y = x):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __rsub__(self, other):
        return Vec(other.x - self.x, other.y - self.y)

    def __mul__(self, other):
        if isinstance(other, Vec):
            return Vec(self.x * other.x, self.y * other.y)
        if isinstance(other, int) or isinstance(other, float):
            return Vec(self.x * other, self.y * other)

    def __rmul__(self, other):
        if isinstance(other, Vec):
            return Vec(self.x * other.x, self.y * other.y)
        if isinstance(other, int) or isinstance(other, float):
            return Vec(self.x * other, self.y * other)

    def __truediv__(self, other):
        try:
            if isinstance(other, Vec):
                return Vec(self.x / other.x, self.y / other.y)
            if isinstance(other, int) or isinstance(other, float):
                return Vec(self.x / other, self.y / other)
        except ZeroDivisionError:
            return Vec(0)

    def __rdiv__(self, other):
        try:
            if isinstance(other, Vec):
                return Vec(other.x / self.x, other.y / self.y)
            if isinstance(other, int) or isinstance(other, float):
                return Vec(other / self.x, other / self.y)
        except ZeroDivisionError:
            return Vec(0)

    def __round__(self):
        return Vec(round(self.x), round(self.y))

    def rot(self, a: int):
        """повернуть по всем осям
        :param a:
        """

        self.x = self.x * cos(a) - self.y * sin(a)
        self.y = -self.x * sin(a) + self.y * cos(a)

    @property
    def get(self):
        return self.x, self.y

    @property
    def size(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

    @property
    def angle(self):
        return acos(scal(Vec(0, 1), self) / self.size)


def distance(a, b):
    return ((b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y)) ** 0.5


def norm(vec):
    return vec / vec.size


def scal(a, b):
    return a.x * b.x + a.y * b.y


def from_angle(a):
    res = Vec(sin(a), cos(a))
    return res
