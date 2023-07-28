from applications.book import Book


def test_json():
    book = Book("Dorothy", "The wonderful world of os", "67", "904757363")

    expected = dict(
        _id=None,
        author="Dorothy",
        title="The wonderful world of os",
        pages="67",
        isbn="904757363",
    )

    assert expected == book.json