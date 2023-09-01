class Tags:
    def __init__(self, id: int, tag: str) -> None:
        self.id = id
        self.tag = tag

    def __str__(self) -> None:
        return f"ID: {self.id}\nTAG: {self.tag}"