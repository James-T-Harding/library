from applications.book import Book, BookList


book1 = Book("John Johnson", "Book Title", "200", "1235433865")
book2 = Book("Dorothy", "The wonderful world of os", "67", "904757363")


def get_books():
    book_list = BookList(book1, book2)
    book_list.update_ids()

    return book_list


def test_get():
    books = get_books()

    assert books.get(1) == book1


def test_delete():
    books = get_books()
    books.delete(1)

    assert books.filter() == [book2]


def test_update():
    books = get_books()
    books.update(2, title="The wonderful world of oz")

    assert books.get(2).title == "The wonderful world of oz"


def test_create():
    books = get_books()
    book = books.create("John Jackson", "Book Title 2", "200", "1235433866")

    assert book.id == 3
    assert book.author == "John Jackson"
    assert book.title == "Book Title 2"
    assert book.pages == "200"
    assert book.isbn == "1235433866"


def test_filter():
    books = get_books()
    assert books.filter(author="John Johnson") == [book1]


def test_update_ids():
    get_books()

    assert book1.id == 1
    assert book2.id == 2
