"""
The Factory Method Pattern defines an interface for creating an object, but
lets subclasses decide which class to instantiate. Factory Method lets a class
defer instantiation to subclasses.
"""
class FrenchLocalizer:
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}

    def localize(self, msg):
        return self.translations.get(msg, msg)


class SpanishLocalizer:
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}

    def localize(self, msg):
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    def localize(self, msg):
        return msg


def main():
    f = FrenchLocalizer()
    s = SpanishLocalizer()
    e = EnglishLocalizer()

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(s.localize(msg))
        print(e.localize(msg))


if __name__ == "__main__":
    main()
