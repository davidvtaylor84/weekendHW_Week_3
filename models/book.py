from xmlrpc.client import boolean


class Book:
    def __init__(self, book_title, author, genre, isbn, summary, status):
        self.book_title = book_title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.summary = summary
        self.status = status

    