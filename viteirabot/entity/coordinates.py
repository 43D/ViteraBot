class Coordinates:
    def __init__(self, id: int, x_start: int, y_start: int, x_end: int, y_end: int) -> None:
        self.id = id
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end

    def __str__(self) -> None:
        return f"ID: {self.id}\nX,Y start: ({self.x_start},{self.y_start})\nX,Y END: ({self.x_end},{self.y_end})"