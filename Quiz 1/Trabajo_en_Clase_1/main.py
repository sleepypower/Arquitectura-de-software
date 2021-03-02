from abc import ABC, abstractmethod

"""
Invoker: Bot
Commands: 
"""

class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

class EncenderCommand(Command):

    def __init__(self):
        pass

    def execute(self) -> None:
        print("Encendiendo!")

class ApagarCommand(Command):

    def __init__(self):
        pass

    def execute(self) -> None:
        print("Apagando!")


class HablarCommand(Command):

    def __init__(self, message):
        self.message = message

    def execute(self) -> None:
        print(f"Bot dice: {self.message}")


class Bot:

    def encender(self, command):
        self.comando_enceder = command

    def apagar(self, command):
        self.comando_apagar = command


