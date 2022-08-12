import unittest

from models.book import Book


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = Book("Do Androids Dream of Electric Sheep", "Philip K. Dick", "Science-Fiction")
        self.book2 = Book("Soul Keeping Company", "Lucie Brock-Broido", "Poetry")
        self.book3 = Book("Wide Sargasso Sea", "Jean Rhys", "Fiction")
        self.book4 = Book("Renegade", "Mark E. Smith", "Biography")
        self.book5 = Book("Blood Meridian", "Cormac McCarthy", "Fiction")
        self.book6 = Book("The Melancholy of Resistance", "László Krasznahorkai", "Fiction")
        self.book7 = Book("Inverted World", "Christopher Priest", "Science-Fiction")
        self.book8 = Book("The Vorhh", "Brian Catling", "Fantasy")

        self.booklist = [self.book1, self.book2, self.book3, self.book4, self.book5, self.book6, self.book7, self.book8]

    # set-up tests
    def test_books_have_name(self):
        self.assertEqual("Do Androids Dream of Electric Sheep", self.book1.book_title)  

    def test_books_have_author(self):
        self.assertEqual("Brian Catling", self.book8.author)
    
    def test_books_have_genre(self):
        self.assertEqual("Fiction", self.book5.genre)