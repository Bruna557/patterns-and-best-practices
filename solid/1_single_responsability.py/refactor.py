"""
Every module should have one, and only one, reason to change.

Gather together the things that change for the same reasons. Separate things
that change for different reasons.

Rule of thumb: if you can't describe what a function does without using words
like "then" or "and", you might be violating the SRP.
"""

"""
Example that doesn't break SRP: we create a separate SumOutputter class and use
that new class to handle the logic you need to output the data to the user.
"""
import json
import math


class Square:
    def __init__(self, length: float) -> None:
        self.length = length


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius


class AreaCalculator:
    def __init__(self, shapes: list) -> None:
        self.shapes = shapes

    def sum(self) -> float:
        areas = []
        for shape in self.shapes:
            if type(shape) is Square:
                areas.append(shape.length**2)
            if type(shape) is Circle:
                areas.append(math.pi * shape.radius**2)
        return sum(areas)


class SumOutputter:
    def __init__(self, sum) -> None:
        self.sum = sum

    def text_output(self) -> str:
        return f"Sum of the areas: {self.sum()}"

    def json_output(self) -> object:
        data = {
            "sum": self.sum
        }
        return json.dumps(data)


if __name__ == "__main__":
    area_calculator = AreaCalculator([
        Square(2),
        Circle(5)
    ])
    sum_outputter = SumOutputter(area_calculator.sum())
    print(sum_outputter.json_output())
