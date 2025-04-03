import dataclasses
import logging
import os

from app.data import BookRepo, CsvDataSource


@dataclasses.dataclass
class App:
    repo: BookRepo


def bootstrap() -> App:
    kwargs = {
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "level": getattr(logging, os.getenv("LOGGER_LEVEL", "INFO"))
    }
    logging.basicConfig(**kwargs)
    return App(BookRepo(CsvDataSource("./data/hugo_winners.csv")))
