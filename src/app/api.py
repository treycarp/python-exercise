from flask import Flask, abort, jsonify, request

from app.boot import bootstrap
from app.data import BookParams

app = bootstrap()
api = Flask(__name__)


@api.route("/book", methods=["GET"])
def book_list():
    return app.repo.fetch_all(BookParams.from_dict(request.args.to_dict()))


@api.route("/book/<int:book_id>", methods=["GET"])
def book_detail(book_id: int):
    book = app.repo.fetch_one(book_id)
    if book is None:
        abort(404)
    else:
        return jsonify(book)


@api.route("/", methods=["GET"])
def health_check():
    return ":)"
