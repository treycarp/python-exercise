from __future__ import annotations
import csv
from abc import ABC, abstractmethod
from typing import List, Dict, Self

from app.domain import Book


class DataSource(ABC):

    @abstractmethod
    def get_all(self) -> List[Book]:
        pass

    @abstractmethod
    def get_one(self, id_: int) -> Book | None:
        pass


class CsvDataSource(DataSource):
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


class BookParams:

    def __init__(self, year: int | None = None):
        self.year = year

    @staticmethod
    def from_dict(d: Dict[str, str]) -> BookParams:
        kwargs = {}
        if d.get("year") is not None:
            kwargs["year"] = int(d["year"])
        return BookParams(**kwargs)


class BookRepo:

    def __init__(self, data_source: DataSource):
        self._data_source = data_source

    def fetch_all(self, params: BookParams) -> List[Book]:
        if params.year is not None:
            return [d for d in self._data_source.get_all() if d.year == params.year]
        else:
            return self._data_source.get_all()

    def fetch_one(self, id_: int) -> Book | None:
        return self._data_source.get_one(id_)
