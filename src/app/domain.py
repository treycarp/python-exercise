import dataclasses


@dataclasses.dataclass
class Book:
    author: str
    id: int
    title: str
    year: int
