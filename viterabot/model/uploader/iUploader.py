from typing import Protocol

class iUploader(Protocol):
    def uploadImage(self, message: str, filename: str) -> None:
        ...