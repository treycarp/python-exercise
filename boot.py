import dataclasses

from data import BookRepo, CsvDataSource


@dataclasses.dataclass
class App:
    repo: BookRepo


def bootstrap() -> App:
    return App(BookRepo(CsvDataSource("hugo_winners.csv")))
