class Duck:
    def fly(self):
        print("Fly")


class CityDuck(Duck):
    pass


class WildDuck(Duck):
    def fly(self):
        print("Wild fly")


class RubberDuck(Duck):
    """
    Because Rubber duck is a duck, it must implement have a fly method, even
    though it doesn't fly
    """
    def fly(self):
        print("No fly")


class MoutainDuck(Duck):
    """
    Code duplication because inheritance is not good for sharing behavior
    horizontally
    """
    def fly(self):
        print("Wild fly")
