class Observer:
    def __init__(self, objectClass) -> None:
        self._objectClass = objectClass

    def update(self, message: str) -> None:
        self._objectClass.doAction(message)