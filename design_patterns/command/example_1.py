"""
The Command Pattern encapsulates a request as an object, thereby letting you
parameterize other objects with different requests, queue or log requests, and
support undoable operations.
"""
from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class CommandImplementation(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.perform_action()


class Receiver:
    def perform_action(self):
        print('Action performed in receiver.')


class Invoker:
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


if __name__ == "__main__":
    receiver = Receiver()
    cmd = CommandImplementation(receiver)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
