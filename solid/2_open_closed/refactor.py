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
import json
import math
from typing import List


class Shape(ABC):
    @property
    @abstractmethod
    def area(self) -> float:
        pass


class Square(Shape):
    def __init__(self, length: float) -> None:
        self.length = length

    @property
    def area(self) -> float:
        return self.length**2


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def area(self) -> float:
        return math.pi * self.radius**2


class AreaCalculator:
    def __init__(self, shapes: List[Shape]) -> None:
        self.shapes = shapes

    def sum(self) -> float:
        areas = []
        for shape in self.shapes:
            areas.append(shape.area)
        return sum(areas)


if __name__ == "__main__":
    area_calculator = AreaCalculator([
        Square(2),
        Circle(5)
    ])
    print(area_calculator.sum())
