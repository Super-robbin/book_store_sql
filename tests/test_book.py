from lib.book import Book

"""
Book construct with id, title, author_name
"""
def test_book_construct():
    book = Book(1, 'My title', 'My author name')
    assert book.id == 1
    assert book.title == 'My title'
    assert book.author_name == 'My author name'

"""
Format the Book to string nicely
"""
def test_book_format_nicely():
    book = Book(1, 'My title', 'My author name')
    assert str(book) == 'Book(1, My title, My author name)'

"""
We can compare two identical books
And have them be equal.
"""
def test_equal_books():
    book1 = Book(1, 'My title', 'My author name')
    book2 = Book(1, 'My title', 'My author name')
    assert book1 == book2