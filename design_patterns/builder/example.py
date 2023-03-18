"""
The Builder Pattern lets you construct complex objects step by step. It allows
you to produce different types and representations of an object using the same
construction code.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self):
        product = self._product
        """
        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add("PartA1")

    def produce_part_b(self):
        self._product.add("PartB1")

    def produce_part_c(self):
        self._product.add("PartC1")


class Product1:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return print(f"Products parts: {', '.join(self.parts)}")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self):
        self.builder = None

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_minimal_viable_product(self):
        self.builder.produce_part_a()

    def build_full_featured_product(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    builder = ConcreteBuilder1()
    director = Director()
    director.builder = builder

    director.build_minimal_viable_product()
    builder.product.list_parts()

    director.build_full_featured_product()
    builder.product.list_parts()

    # Custom product (remember - the Director class is optional)
    builder.produce_part_b()
    builder.produce_part_c()
    builder.product.list_parts()
