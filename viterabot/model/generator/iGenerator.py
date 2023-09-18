from typing import Protocol

class iGenerator(Protocol):
    def generate(self) -> str:
        ...
