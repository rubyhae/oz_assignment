from flask_smorest import Blueprint, abort
from flask import request
from schemas import BookSchema

blp = Blueprint("books", "books", url_prefix="/api/v1", description="Operations on books")

books = []

@blp.route("/feeds", methods=["GET"])
def get_books():
    return {"result": "success", "data": books}

@blp.route("/feeds", methods=["POST"])
@blp.arguments(BookSchema)
def add_book(new_book):
    books.append(new_book)
    return {"result": "success", "data": new_book}, 201

@blp.route("/feeds/<string:title>", methods=["PUT"])
@blp.arguments(BookSchema)
def update_book(new_data, title):
    for book in books:
        if book["title"] == title:
            book.update(new_data)
            return {"result": "success", "data": book}
    abort(404, message="Book not found")

@blp.route("/feeds/<string:title>", methods=["DELETE"])
def delete_book(title):
    global books
    books = [book for book in books if book["title"] != title]
    return {"result": "success", "message": "Book deleted"}
