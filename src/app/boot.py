import dataclasses

from app.data import BookRepo, CsvDataSource


@dataclasses.dataclass
class App:
    repo: BookRepo


def bootstrap() -> App:
    return App(BookRepo(CsvDataSource("./data/hugo_winners.csv")))
