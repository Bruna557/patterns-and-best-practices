'''
A client should never be forced to implement an interface that it doesn't use,
or clients shouldn't be forced to depend on methods they do not use.

Keep interfaces small so that users don't end up depending on things they don't
need.

Several specific interfaces are better than one generic interface.
'''

'''
Example that doesn't violate the Interface Segregation Principle: we create a
second interface
'''
class Shape:
    @property
    def area(self):
        raise NotImplementedError


class ThreeDimensionalShape(Shape):
    @property
    def volume(self):
        raise NotImplementedError


class Cube(ThreeDimensionalShape):
    def __init__(self, length):
        self.length = length

    @property
    def area(self):
        return 6 * self.length**2

    @property
    def volume(self):
        return self.length**3


class Square(Shape):
    def __init__(self, length):
        self.length = length

    @property
    def area(self):
        return self.length**2
