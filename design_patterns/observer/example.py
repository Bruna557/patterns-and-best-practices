"""
The Observable Pattern defines a one-to-many dependency between objects, so
that when one object (the observable) changes state, all of its dependencies (
the observers) are notified and updated automatically.
"""

""" Observable"""
class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = 0

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def set_temperature(self, temp):
        self.temperature = temp
        self.notify()


"""Observers"""

class SmartPhone:
    def __init__(self, weather_station):
        """
        We pass the observable to the observer so we can access the state (thus
        the update methods doesn't need any parameters)
        """
        self.weather_station = weather_station

    def display(self):
        print(f"SmartPhone: {self.weather_station.temperature}")

    def update(self):
        self.display()

class Lcd:
    def __init__(self, weather_station):
        self.weather_station = weather_station

    def display(self):
        print(f"Lcd: {self.weather_station.temperature}")

    def update(self):
        self.display()


station = WeatherStation()
phone = SmartPhone(station)
lcd = Lcd(station)
station.register_observer(phone)
station.register_observer(lcd)
station.unregister_observer(lcd)
station.set_temperature(23.7)
