import unittest

from models.book import Book
from models.book_list import *


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = Book("Do Androids Dream of Electric Sheep", "Philip K. Dick", "Science-Fiction", 9781439447093, "Do Androids Dream of Electric Sheep? is a dystopian science fiction novel by American writer Philip K. Dick, first published in 1968. The novel is set in a post-apocalyptic San Francisco, where Earth's life has been greatly damaged by a nuclear global war, leaving most animal species endangered or extinct.")

        self.book2 = Book("Soul Keeping Company", "Lucie Brock-Broido", "Poetry", 9789402617030, "Soul Keeping Company' contains a selection of poetry from the pen of Lucy Brock-Broido.")

        self.book3 = Book("Wide Sargasso Sea", "Jean Rhys", "Fiction", 9789923294680, "Wide Sargasso Sea is a 1966 novel by Dominican-British author Jean Rhys. The novel serves as a postcolonial and feminist prequel to Charlotte Brontë's novel Jane Eyre, describing the background to Mr. Rochester's marriage from the point-of-view of his wife Antoinette Cosway, a Creole heiress.")

        self.book4 = Book("Renegade", "Mark E. Smith", "Biography", 9784180374991, "The only way to appreciate the legendary musician Mark E. Smith is to encounter the man in his own words.")

        self.book5 = Book("Blood Meridian", "Cormac McCarthy", "Fiction", 9787206208987, "Blood Meridian or the Evening Redness in the West is a 1985 epic novel by American author Cormac McCarthy, classified under the Western, or sometimes the anti-Western, genre. McCarthy's fifth book, it was published by Random House.")

        self.book6 = Book("The Melancholy of Resistance", "László Krasznahorkai", "Fiction", 9785970737620, "Hungarian writer László Krasznahorkai. The narrative is set in a restless town where a mysterious circus, which exhibits a whale and nothing else, contributes to an apocalyptic atmosphere.")

        self.book7 = Book("Inverted World", "Christopher Priest", "Science-Fiction", 9785168327602, "Inverted World is a 1974 science fiction novel by British writer Christopher Priest. The novel's basic premise was first used in the short story, The Inverted World, included in New Writings in SF 22, which had different characters and plot. In 2010, the novel was included in the SF Masterworks collection.")

        self.book8 = Book("The Vorhh", "Brian Catling", "Fantasy", 9787869285564, "The Vorrh is a dark historical fantasy novel by multi-disciplinary artist B. Catling that was first published in November of 2012.")

        self.new_book = Book("10:04", "Ben Lerner", "Fiction", 9787206208763, "New novel by Ben Lerner")

        self.booklist = [self.book1, self.book2, self.book3, self.book4, self.book5, self.book6, self.book7, self.book8]

    # set-up tests
    def test_books_have_name(self):
        self.assertEqual("Do Androids Dream of Electric Sheep", self.book1.book_title)  

    def test_books_have_author(self):
        self.assertEqual("Brian Catling", self.book8.author)
    
    def test_books_have_genre(self):
        self.assertEqual("Fiction", self.book5.genre)

    # def test_add_new_book(self):
    #     add_book = self.booklist.add_new_book(self.new_book.book_title)
    #     self.assertEqual(["10:04"], add_book)
