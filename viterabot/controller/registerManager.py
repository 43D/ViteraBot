from viterabot.observer.iObserverAction import iObserverAction

class RegisterManager(iObserverAction):
    def __init__(self) -> None:
        self.running = True
        self.command = {
            "done": self.done
        }

    def doAction(self, message: str) -> None:
        if self.command.get(message) is not None:
            self.command[message]()

    def done(self) -> None:
        self.running = False
