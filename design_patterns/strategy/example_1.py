"""
Strategy Pattern defines a family of algorithms, it encapsulates each one of
them and makes them interchangeable (you can plug and play - sometimes use
algorithm A, sometimes use algorithm B...).
Strategy lets the algorithm vary independently from the clients that use it (
you change the algorithm without changing the client).
"""
from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self) -> None:
        pass


class Duck:
    def __init__(self, qb: QuackBehavior) -> None:
        self.quack_behavior = qb

    def quack(self) -> None:
        self.quack_behavior.quack()


class StandardQuack(QuackBehavior):
    def quack(self) -> None:
        print("Quack!")


class Squeak(QuackBehavior):
    def quack(self) -> None:
        print("Squeak!")


wild_duck = Duck(StandardQuack())
wild_duck.quack()

rubber_duck = Duck(Squeak())
rubber_duck.quack()
