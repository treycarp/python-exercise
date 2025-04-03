import logging

from flask import Flask, abort, jsonify, request

from app.boot import bootstrap
from app.data import BookParams


logger = logging.getLogger(__name__)
app = bootstrap()
api = Flask(__name__)


@api.route("/book", methods=["GET"])
def book_list():
    query_params = request.args.to_dict()
    logging.debug(f"book_list: {query_params}")
    return app.repo.fetch_all(BookParams.from_dict(query_params))


@api.route("/book/<int:book_id>", methods=["GET"])
def book_detail(book_id: int):
    logging.debug(f"book_detail: {book_id}")
    book = app.repo.fetch_one(book_id)
    if book is None:
        abort(404)
    else:
        return jsonify(book)


@api.route("/", methods=["GET"])
def health_check():
    logging.debug("health_check")
    return ":)"
