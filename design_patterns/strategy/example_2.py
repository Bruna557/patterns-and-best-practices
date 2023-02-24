"""
Strategy Pattern defines a family of algorithms, it encapsulates each one of
them and makes them interchangeable (you can plug and play - sometimes use
algorithm A, sometimes use algorithm B...).
Strategy lets the algorithm vary independently from the clients that use it (
you change the algorithm without changing the client).
"""

class Item:
    def __init__(self, price, discount_strategy = None):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        return self.price - discount

    def __repr__(self):
        return f"Price: {self.price}, price after discount: {self.price_after_discount()}"


def on_sale_discount(order):
    return order.price * 0.25 + 20


def twenty_percent_discount(order):
    return order.price * 0.20


print(Item(20000))
print(Item(20000, discount_strategy = twenty_percent_discount))
print(Item(20000, discount_strategy = on_sale_discount))
