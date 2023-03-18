from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):
    def notify(self, message, email):
        print(f"Send '{message}' to {email}")


class SMS(Notification):
    def notify(self, message, phone):
        print(f"Send '{message}' to {phone}")


notification = SMS()
notification.notify("Hello", "john@test.com")