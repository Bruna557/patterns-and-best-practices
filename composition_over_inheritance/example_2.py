"""
Imagine we have the following:

    Robot
        .drive()

        CleaningRobot
            .clean()

        MurderRobot
            .kill()

    Animal
        .poop()

        Dog
            .bark()

        Cat
            .meow()

And now we need a MurderRobotDog that drives, barks and kill but doesn't poop.

Using composition, we would do this:
    dog = pooper + barker
    cat = pooper + meower
    cleaningRobot = driver + cleaner
    murderRobot = driver + killer
    murderRobotDog = driver + killer + barker
"""
class Driver:
    def drive(self):
        print("Drive")


class Killer:
    def kill(self):
        print("Kill")


class Barker:
    def bark(self):
        print("Bark")


class MurderRobotDog:
    driver: Driver
    killer: Killer
    barker: Barker

    def __init__(self, driver: Driver, killer: Killer, barker: Barker):
        self.driver = driver
        self.killer = killer
        self.barker = barker

    def drive(self):
        self.driver.drive()

    def kill(self):
        self.killer.kill()

    def bark(self):
        self.barker.bark()


d = Driver()
k = Killer()
b = Barker()
murder_robot_dog = MurderRobotDog(d, k, b)
murder_robot_dog.bark()
