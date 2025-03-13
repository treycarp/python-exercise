from flask import Flask, abort, jsonify

from boot import bootstrap

app = bootstrap()
api = Flask(__name__)


@api.route("/book", methods=["GET"])
def book_list():
    return app.repo.fetch_all()


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
