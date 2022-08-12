from flask import render_template, request, redirect, url_for 
from app import app
from models.book import Book
from models.book_list import booklist

@app.route('/library')
def library_main():
    return render_template('index.html',title = "Library", booklist = booklist)

@app.route('/library/<int:index>')
def specific_book(index):
    return render_template('specific_book.html', title = 'Book Details', booklist = booklist[index])

@app.route('/library/add_new')
def new():
    return render_template('add_new.html')

@app.route('/add_new', methods =['POST'])
def new_book():
    book_title = request.form['book_title']
    author = request.form['author']
    genre = request.form['genre']
    isbn = request.form['isbn']
    summary = request.form['summary']
    new_book = Book(book_title, author, genre, isbn, summary)
    booklist.append(new_book)
    return redirect('/library')

