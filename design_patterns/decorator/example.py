"""
The Decorator Pattern attaches aditional responsabilities to an object
dynamically (at compile time or at runtime). Decorators provide a flexible
alternative to subclassing for extending functionality.
"""

"""
Keep in mind the example below is not a good use case for the decorator
pattern; the the decorators have similar implementation and the problem could
have been solved with iteration in the cost function (see better_solution.py)
"""
from abc import ABC, abstractmethod


class Beverage(ABC):
    @property
    @abstractmethod
    def cost(self):
        pass


class Espresso(Beverage):
    @property
    def cost(self):
        return 1


class Decaf(Beverage):
    @property
    def cost(self):
        return 2


class AddOnDecorator(Beverage):
    @property
    @abstractmethod
    def cost(self):
        pass


class CaramelDecorator(AddOnDecorator):
    """
    The decorator both IS a beverage (this allows us to have multiple layers of
    decorators wrapping a beverage) and HAS a beverage.
    """

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    @property
    def cost(self):
        return self.beverage.cost + 2


class WhippedCreamDecorator(AddOnDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    @property
    def cost(self):
        return self.beverage.cost + 3


b = CaramelDecorator(WhippedCreamDecorator(Espresso()))
print(b.cost)
