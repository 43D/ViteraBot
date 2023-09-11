from abc import ABC, abstractmethod

class iGenerator(ABC):
    @abstractmethod
    def generateText(self) -> str:
        pass
