import threading
import os
from viterabot.observer.iObserverAction import iObserverAction


class RegisterManager(iObserverAction):
    def __init__(self, eventRegister: threading.Event) -> None:
        self.eventRegister = eventRegister
        self.running = True

    def _clearConsole(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def _inputCommand(self) -> None:
        try:
            print("executando P: ")
            self._clearConsole()
            x = input("teste: ")
            print('Hello, ' + x)
            # execute register
        except:
            pass

    def runRegister(self) -> None:
        self.eventRegister.wait()
        while self.running:
            self._inputCommand()
            self.eventRegister.clear()
            self.eventRegister.wait()

    def doAction(self, message: str) -> None:
        if message == "done":
            self.done()

    def done(self) -> None:
        self.running = False
