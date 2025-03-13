import dataclasses

from data import BookRepo


@dataclasses.dataclass
class App:
    repo: BookRepo


def bootstrap() -> App:
    return App(BookRepo())
