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
    def __init__(self, len: int):
        self.length = len


class Circle:
    def __init__(self, rad: int):
        self.radius = rad


class AreaCalculator:
    def __init__(self, shapes: []):
        self.shapes = shapes

    def sum(self):
        areas = []

        for shape in self.shapes:
            if type(shape) is Square:
                areas.append(shape.length**2)
            elif type(shape) is Circle:
                areas.append(math.pi * shape.radius**2)

        return sum(areas)


class SumOutputter:
    def __init__(self, sum):
        self.sum = sum

    def json_output(self):
        data = {
          'sum': self.sum,
        }

        return json.dumps(data);


area_calculator = AreaCalculator([
    Square(4),
    Circle(2)
])
sum_of_areas = area_calculator.sum()
sum_outputter = SumOutputter(sum_of_areas)
print(sum_outputter.json_output())
