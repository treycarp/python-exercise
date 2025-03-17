from app.data import BookParams


def test_book_params_from_dict():
    i = {"year": "2025"}
    o = BookParams.from_dict(i)
    assert o.year == 2025


def test_book_repo_fetch_all():
    pass


def test_book_repo_fetch_all_filter_year():
    pass


def test_book_repo_fetch_one_ok():
    pass


def test_book_repo_fetch_one_none():
    pass


def test_csv_data_source_get_one_ok():
    pass


def test_csv_data_source_get_one_none():
    pass
