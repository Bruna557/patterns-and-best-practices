from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class Duck:
    fly_behavior: FlyBehavior

    def __init__(self, fb: FlyBehavior):
        self.fly_behavior = fb


    def fly(self):
        self.fly_behavior.fly()


class SimpleFly(FlyBehavior):
    def fly(self):
        print("Fly")


class WildFly(FlyBehavior):
    def fly(self):
        print("Wild fly")


wild_duck = Duck(WildFly())
wild_duck.fly()
