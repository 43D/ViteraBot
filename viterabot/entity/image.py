from dataclasses import dataclass


@dataclass(kw_only=True, slots=True, frozen=False)
class Image:
    id: int
    src_path: str
    title: str
    hashImage: str