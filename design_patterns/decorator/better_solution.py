"""
This is a better solution for the problem in example.py without using the
decorator pattern.
"""
import abc


class Beverage(abc.ABC):
    def __init__(self, add_ons: list):
        self.add_ons = add_ons

    def cost(self):
        cost = 0
        for add_on in self.add_ons:
            cost += add_on().cost()
        return cost


class Espresso(Beverage):
    def cost(self):
        return Beverage.cost(self) + 1


class Decaf(Beverage):
    def cost(self):
        return Beverage.cost(self) + 2


class Caramel:
    def cost(self):
        return 2


class WhippedCream:
    def cost(self):
        return 3


b = Espresso([Caramel, WhippedCream])
print(b.cost())
