'''
Every subclass or derived class should be substitutable for their base or
parent class.

That requires the objects of your derived classes to behave in the same way as
the objects of your base class. You can achieve that by following a few rules:
- An overridden method of a derived class needs to accept the same input
parameter values as the method of the base class.
    - That means you can implement less restrictive validation rules, but you
    are not allowed to enforce stricter ones in your derived class.
- The return value of a method of the derived class needs to comply with the
same rules as the return value of the method of the base class.
    - You can only decide to apply even stricter rules by returning a specific
    derived class of the defined return value, or by returning a subset of the
    valid return values of the base class.
'''

'''
Example that violates the Liskov Substitution Principle:
'''
class Duck:
    def quack(self):
        print("Quack!")


class RubberDuck(Duck):
    def quack(self):
        raise Exception("I don't quack")


rubber_duck = RubberDuck()
rubber_duck.quack()


'''
Example that violates the Liskov Substitution Principle:
'''
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def area():
        return self.width * self.length


class Square(Rectangle):
    def __init__(self, length): # violation
        self.length = length

    @property
    def area():
        return self.length**2


square = Square(4)
# rectangle = Rectangle(4)  -- error
