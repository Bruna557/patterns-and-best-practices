'''
Gather together the things that change for the same reasons. Separate things
that change for different reasons.

Every module should have one, and only one, reason to change.

Rule of thumb: if you can't describe what a function does without using words
like "then" or "and", you might be violating the SRP.
'''

'''
Example that violates the Single Responsability Principle:

AreaCalculator handles the logic to output the data.
Consider a scenario where the output should be converted to another format like
JSON.
The AreaCalculator class should only be concerned with the sum of the areas of
provided shapes.

To address this, we can create a separate SumCalculatorOutputter class and use
that new class to handle the logic we need to output the data to the user.
'''
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

    def output(self):
        return "Sum of the areas: " + str(self.sum())


area_calculator = AreaCalculator([
    Square(4),
    Circle(2)
])
print(area_calculator.output())
