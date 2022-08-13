from operator import index
from flask import render_template, request, redirect, url_for 
from app import app
from models.book import Book
from models.book_list import add_new_book, delete_book, booklist

@app.route('/library')
def library_main():
    return render_template('index.html',title = "Catalogue", booklist = booklist)

@app.route('/library/<int:index>')
def specific_book(index):
    return render_template('specific_book.html', title = 'Book Details', booklist = booklist[index])

@app.route('/library/add_new')
def new():
    return render_template('add_new.html', title = "Add New Book")

@app.route('/add_new', methods =['POST'])
def new_book():
    book_title = request.form['book_title']
    author = request.form['author']
    genre = request.form['genre']
    isbn = request.form['isbn']
    summary = request.form['summary']
    new_book = Book(book_title, author, genre, isbn, summary)
    add_new_book(new_book)
    return redirect('/library')

# @app.route('/library/delete')
# def delete_form():
#     return render_template('delete_book.html', title = "Delete Book")

@app.route('/library/<int:index>', methods =["POST"])
def delete(index):
    delete_book(index)
    return redirect('/library')
    

