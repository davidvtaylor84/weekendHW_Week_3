from flask import render_template, request, redirect, url_for 
from app import app
from models.book import Book
from models.book_list import booklist

@app.route('/library')
def library_main():
    return render_template('index.html',title = "Library", booklist = booklist)