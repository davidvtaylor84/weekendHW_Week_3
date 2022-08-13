
from .book import Book


book1 = Book("Do Androids Dream of Electric Sheep", "Philip K. Dick", "Science-Fiction", 9781439447093, "Do Androids Dream of Electric Sheep? is a dystopian science fiction novel by American writer Philip K. Dick, first published in 1968. The novel is set in a post-apocalyptic San Francisco, where Earth's life has been greatly damaged by a nuclear global war, leaving most animal species endangered or extinct.")

book2 = Book("Soul Keeping Company", "Lucie Brock-Broido", "Poetry", 9789402617030, "Soul Keeping Company' contains a selection of poetry from the pen of Lucy Brock-Broido.")

book3 = Book("Wide Sargasso Sea", "Jean Rhys", "Fiction", 9789923294680, "Wide Sargasso Sea is a 1966 novel by Dominican-British author Jean Rhys. The novel serves as a postcolonial and feminist prequel to Charlotte Brontë's novel Jane Eyre, describing the background to Mr. Rochester's marriage from the point-of-view of his wife Antoinette Cosway, a Creole heiress.")

book4 = Book("Renegade", "Mark E. Smith", "Biography", 9784180374991, "The only way to appreciate the legendary musician Mark E. Smith is to encounter the man in his own words.")

book5 = Book("Blood Meridian", "Cormac McCarthy", "Fiction", 9787206208987, "Blood Meridian or the Evening Redness in the West is a 1985 epic novel by American author Cormac McCarthy, classified under the Western, or sometimes the anti-Western, genre. McCarthy's fifth book, it was published by Random House.")

book6 = Book("The Melancholy of Resistance", "László Krasznahorkai", "Fiction", 9785970737620, "Hungarian writer László Krasznahorkai. The narrative is set in a restless town where a mysterious circus, which exhibits a whale and nothing else, contributes to an apocalyptic atmosphere.")

book7 = Book("Inverted World", "Christopher Priest", "Science-Fiction", 9785168327602, "Inverted World is a 1974 science fiction novel by British writer Christopher Priest. The novel's basic premise was first used in the short story, The Inverted World, included in New Writings in SF 22, which had different characters and plot. In 2010, the novel was included in the SF Masterworks collection.")

book8 = Book("The Vorhh", "Brian Catling", "Fantasy", 9787869285564, "The Vorrh is a dark historical fantasy novel by multi-disciplinary artist B. Catling that was first published in November of 2012.")

booklist = [book1, book2, book3, book4, book5, book6, book7, book8]

def add_new_book(book):
    booklist.append(book)

# def delete_book(title):
#     book_to_delete = None
#     for book in booklist: 
#         if book.book_title == title:
#             book_to_delete = book
#             break
#     booklist.remove(title)

# def delete_book(index_position):
#     index_position = booklist.index
#     for book in booklist:
#         if book == index_position:
#             booklist.remove(index_position)

# def delete_book(book_to_be_deleted):
#     if book_to_be_deleted in booklist:
#         booklist.remove(book_to_be_deleted)

# def delete_book(book_title, author):
#     if book_title and author in booklist:
#         booklist.remove(book_title, author)

def delete_book(index):
    book_to_delete = None
    for book in booklist:
        if booklist.index == index:
            book_to_delete = book
        break

    booklist.remove(book_to_delete)

# def delete_event(event_name):
#     event_to_delete = None
#     for event in events:
#         if event.name == event_name:
#             event_to_delete = event
#             break

#     events.remove(event_to_delete)