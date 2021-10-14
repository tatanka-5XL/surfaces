# classes.py

from math import pi

class Square:
    def __init__(self, a):
        self.a = a   

    def surface(self):
        return self.a ** 2


class Rectangle(Square):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def surface(self):
        return self.a * self.b


class Triangle:
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def surface(self):
        return self.a * self.h / 2


class Trapezoid(Triangle):
    def __init__(self, a, c, h):
        super().__init__(a, h)
        self.c = c

    def surface(self):
        return ((self.a + self.c) * self.h) / 2


class Circle:
    def __init__(self, r):
        self.r = r

    def surface(self):
        return pi * self.r ** 2
