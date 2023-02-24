'''
Strategy Pattern defines a family of algorithms, it encapsulates each one of
them and makes them interchangeable (you can plug and play - sometimes use
algorithm A, sometimes use algorithm B...).
Strategy lets the algorithm vary independently from the clients that use it (
you change the algorithm without changing the client).
'''
import abc


class QuackBehavior(abc.ABC): # Abstract strategy
	@abc.abstractmethod
	def quack(self):
		pass


class Duck(abc.ABC):
	quack_behavior: QuackBehavior

	def __init__(self, qb: QuackBehavior):
		self.quack_behavior = qb

	def quack(self):
		self.quack_behavior.quack()


class SimpleQuack(QuackBehavior): # Concrete strategy
	def quack(self):
		print("Quack!")


class Squeak(QuackBehavior): # Concrete strategy
	def quack(self):
		print("Squeak!")


wild_duck = Duck(SimpleQuack())
wild_duck.quack()

rubber_duck = Duck(Squeak())
rubber_duck.quack()
