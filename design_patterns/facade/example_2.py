"""
The Façade Pattern provides a unified interface to a set of interfaces in a
subsystem. Façade defines a higher level interface that makes the subsystem
easier to use.
"""
class Subsystem1:
    def prepare(self) -> None:
        print("Subsystem1 - ready")

    def execute(self) -> None:
        print("Subsystem1 - executing")


class Subsystem2:
    def prepare(self) -> None:
        print("Subsystem2 - ready")

    def execute(self) -> None:
        print("Subsystem2 - executing")


class Facade:
    def __init__(self, s1=None, s2=None) -> None:
        self.subsystem1 = s1 or Subsystem1()
        self.subsystem2 = s2 or Subsystem2()

    def execute(self):
        print("Starting subsystems")
        self.subsystem1.prepare()
        self.subsystem2.prepare()
        print("Executing")
        self.subsystem1.execute()
        self.subsystem2.execute()


if __name__ == "__main__":
    facade = Facade()
    facade.execute()
