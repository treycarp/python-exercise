import pytest
from app.api import api


@pytest.fixture()
def app():
    yield api


@pytest.fixture()
def client(app):
    return app.test_client()


def test_book_detail_200(client):
    res = client.get("/book/1")
    assert res.status_code == 200


def test_book_detail_404(client):
    res = client.get("/book/0")
    assert res.status_code == 404


def test_book_list_200(client):
    res = client.get("/book")
    assert res.status_code == 200


def test_book_list_year_param_200(client):
    res = client.get("/book?year=2024")
    assert res.status_code == 200


def test_health_check_200(client):
    res = client.get("/")
    assert res.status_code == 200
