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
    

# Receivers

class LivingRoomLamp:
    def turn_on(self):
        print("Living room light is on")

    def turn_off(self):
        print("Living room light is off")


class LivingRoomAudioSystem:
    def turn_on(self):
        print("Living room audio system is on")

    def turn_off(self):
        print("Living room audio system is off")

# Commands

class TurnLightOn(Command):
    def __init__(self, lamp):
        self.lamp = lamp

    def execute(self):
        self.lamp.turn_on()

    def unexecute(self):
        self.lamp.turn_off()


class TurnAudioSystemOn(Command):
    def __init__(self, radio_system):
        self.radio_system = radio_system

    def execute(self):
        self.radio_system.turn_on()

    def unexecute(self):
        self.radio_system.turn_off()


class TurnLightAndAudioSystemOn(TurnLightOn, TurnAudioSystemOn):
    def __init__(self, lamp, radio_system):
        self.lamp = lamp
        self.radio_system = radio_system

    def execute(self):
        TurnLightOn.execute(self)
        TurnAudioSystemOn.execute(self)

    def unexecute(self):
        TurnLightOn.unexecute(self)
        TurnAudioSystemOn.unexecute(self)


# Invoker
class RemoteControl:
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()

    def unexecute(self):
        self.cmd.unexecute()


lamp = LivingRoomLamp()
radio = LivingRoomAudioSystem()
cmd = TurnLightAndAudioSystemOn(lamp, radio)
remote_control = RemoteControl()
remote_control.cmd = cmd
cmd.execute()
cmd.unexecute()
