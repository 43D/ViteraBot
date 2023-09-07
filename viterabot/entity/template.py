from dataclasses import dataclass


@dataclass(kw_only=True, slots=True, frozen=False)
class Template:
    id: int
    src_path: str