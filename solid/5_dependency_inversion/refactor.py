"""
High-level modules should not depend on low-level modules. Both should depend
on abstractions.

Abstractions should not depend on details. Details should depend on
abstractions.

The dependency inversion principle aims to reduce the coupling between classes
by creating an abstraction layer between them.
"""
from abc import ABC, abstractmethod


class CurrencyConverter(ABC):
    @abstractmethod
    def convert(self, from_currency, to_currency, amount) -> str:
        pass


class FxConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> str:
        return f"{amount} {from_currency} = {amount*1.2} {to_currency}"


class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        print(self.converter.convert("EUR", "USD", 100))


if __name__ == "__main__":
    converter = FxConverter()
    app = App(converter)
    app.start()
