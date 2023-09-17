from typing import Protocol

class iGenerator(Protocol):
    def generateText(self) -> str:
        ...
