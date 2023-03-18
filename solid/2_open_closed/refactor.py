"""
A Module should be open for extension but closed for modification.

Changes to behavior must be made by adding new code instead of modifying
existing code.

Separate extensible behavior behind an interface, and flip the dependencies.
"""

"""
Example that doesn't violates the Open-Closed Principle: we remove the logic to
calculate the area of each shape out of the AreaCalculator class method and
attach it to each shape's class.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, len: int):
        self.length = len

    @property
    def area(self):
        return self.length**2


class Circle(Shape):
    def __init__(self, rad: int):
        self.radius = rad

    @property
    def area(self):
        return math.pi * self.radius**2


class AreaCalculator:
    def __init__(self, shapes: list):
        self.shapes = shapes

    def sum(self):
        return sum(shape.area for shape in self.shapes)


area_calculator = AreaCalculator([
    Square(4),
    Circle(2)
])
print(area_calculator.sum())
