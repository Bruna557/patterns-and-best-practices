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

    @abstractmethod
    def unexecute(self):
        pass


class TurnLightOn(Command):
    def __init__(self, lamp):
        self.lamp = lamp

    def execute(self):
        self.lamp.turn_on()

    def unexecute(self):
        self.lamp.turn_off()


class LivingRoomLamp: # Receiver
    def turn_on(self):
        print('Living room lamp turned on')

    def turn_off(self):
        print('Living room lamp turned off')


class RemoteControl: # Invoker
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()

    def unexecute(self):
        self.cmd.unexecute()


if __name__ == "__main__":
    lamp = LivingRoomLamp()
    cmd = TurnLightOn(lamp)
    remote_control = RemoteControl()
    remote_control.command(cmd)
    remote_control.execute()
    remote_control.unexecute()
