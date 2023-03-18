"""
A Module should be open for extension but closed for modification.

Changes to behavior must be made by adding new code instead of modifying
existing code.

Separate extensible behavior behind an interface, and flip the dependencies.
"""

"""
Example that violates the Open-Closed Principle:
Consider a scenario where the user would like the sum of additional shapes like
triangles, pentagons, hexagons, etc. we would have to constantly edit
AreaCalculator and add more if/else blocks.

A way we can make this sum method better is to remove the logic to calculate
the area of each shape out of the AreaCalculator class method and attach it to
each shape's class.
"""
import math
from typing import List


class Square:
    def __init__(self, length: float) -> None:
        self.length = length


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius


class AreaCalculator:
    def __init__(self, shapes: List) -> None:
        self.shapes = shapes

    def sum(self) -> float:
        areas = []
        for shape in self.shapes:
            if type(shape) is Square:
                areas.append(shape.length**2)
            elif type(shape) is Circle:
                areas.append(math.pi * shape.radius**2)
        return sum(areas)


area_calculator = AreaCalculator([
    Square(2),
    Circle(5)
])
print(area_calculator.sum())
