from dataclasses import dataclass


@dataclass(kw_only=True, slots=True, frozen=False)
class Post:
    id: int
    id_image: int = 0
    id_facebook: int = 0
    discord: bool = False
    published: bool = False