import csv
from typing import List

from domain import Book


class CsvDataSource:
    _data = dict()

    def __init__(self, file_path: str):
        with open(file_path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self._data[int(row["id"])] = self._row_to_model(row)

    def get_all(self) -> List[Book]:
        return list(self._data.values())

    def get_one(self, id_: int) -> Book | None:
        return self._data.get(id_)

    def _row_to_model(self, row: dict[str, str, str, str]) -> Book:
        return Book(
            author=row["author"],
            id=int(row["id"]),
            title=row["title"],
            year=int(row["year"])
        )


class BookRepo:

    def __init__(self):
        self._data_source = CsvDataSource("hugo_winners.csv")

    def fetch_all(self) -> List[Book]:
        return self._data_source.get_all()

    def fetch_one(self, id_: int) -> Book | None:
        return self._data_source.get_one(id_)
