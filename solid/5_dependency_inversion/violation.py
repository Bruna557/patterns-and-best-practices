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
        print(f"{amount} {from_currency} = {amount*1.2} {to_currency}")
        return amount*1.2


class App:
    def start(self):
        converter = FxConverter()
        converter.convert("EUR", "USD", 100)


app = App()
app.start()
