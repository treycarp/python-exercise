import random
from typing import List, Dict

import factory

from app.data import BookParams, DataSource, BookRepo
from app.domain import Book


class MemDataSource(DataSource):

    def __init__(self):
        self._data: Dict[int, Book] = dict()

    def add_book(self, book: Book):
        self._data[book.id] = book

    def get_all(self) -> List[Book]:
        return list(self._data.values())

    def get_one(self, id_: int) -> Book | None:
        return self._data.get(id_)


class BookFactory(factory.Factory):
    class Meta:
        model = Book

    author = factory.Faker("name")
    id = factory.Sequence(lambda n: n)
    title = factory.Faker('sentence', nb_words=4)
    year = random.choice(range(2020, 2024))


def test_book_params_from_dict():
    i = {"year": "2025"}
    o = BookParams.from_dict(i)
    assert o.year == 2025


def test_book_repo_fetch_all():
    data_source = MemDataSource()

    count = 4
    for _ in range(count):
        data_source.add_book(BookFactory.build())

    repo = BookRepo(data_source)
    books = repo.fetch_all()
    assert len(books) == count


def test_book_repo_fetch_all_filter_year():
    data_source = MemDataSource()

    count_a = 2
    for _ in range(count_a):
        data_source.add_book(BookFactory.build(year=2023))

    count_b = 2
    for _ in range(count_b):
        data_source.add_book(BookFactory.build(year=2024))

    repo = BookRepo(data_source)
    params = BookParams(year=2024)
    books = repo.fetch_all(params)
    assert len(books) == count_b


def test_book_repo_fetch_one_ok():
    id_ = 8
    title_ = "testing"
    data_source = MemDataSource()
    data_source.add_book(BookFactory.build(id=id_, title=title_))

    repo = BookRepo(data_source)
    book = repo.fetch_one(id_)
    assert book.title == title_


def test_book_repo_fetch_one_none():
    data_source = MemDataSource()
    repo = BookRepo(data_source)
    book = repo.fetch_one(16)
    assert book is None
