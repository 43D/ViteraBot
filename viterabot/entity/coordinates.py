from dataclasses import dataclass


@dataclass(kw_only=True, slots=True, frozen=False)
class Coordinates:
    id: int
    x_start: int
    y_start: int
    x_size: int
    y_size: int
    rotation: int