from typing import Protocol

class iEditor(Protocol):
    def edit(self, date: dict) -> None:
        ...