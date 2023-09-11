from abc import ABC, abstractmethod

class iUploader(ABC):
    @abstractmethod
    def uploadImage(self, message: str, filename: str) -> None:
        pass