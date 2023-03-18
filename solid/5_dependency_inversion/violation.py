"""
High-level modules should not depend on low-level modules. Both should depend
on abstractions.

Abstractions should not depend on details. Details should depend on
abstractions.

The dependency inversion principle aims to reduce the coupling between classes
by creating an abstraction layer between them.
"""
class FxConverter:
    def convert(self, from_currency, to_currency, amount):
        return f"{amount} {from_currency} = {amount*1.2} {to_currency}"


class App:
    def start(self):
        converter = FxConverter()
        print(converter.convert("EUR", "USD", 100))


if __name__ == "__main__":
    app = App()
    app.start()
