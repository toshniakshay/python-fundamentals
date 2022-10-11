class InvalidPageReadError(ValueError):
    ...


class Book:

    def __init__(self, name: str, page_count: int, page_read: int = 0):
        self.name = name
        self.page_count = page_count
        self.page_read = page_read

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.page_read} pages out of {self.page_count}>"
        )

    def read_book(self, pages: int):
        pages = self.page_read + pages
        if pages > self.page_count:
            raise InvalidPageReadError()
        self.page_count = pages


cleanCode = Book("Clean Code", 500)
try:
    cleanCode.read_book(300)
    cleanCode.read_book(300)
except InvalidPageReadError:
    print("Got the error")
