
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.__qualname__ = "Book"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
        self.__qualname__ = "EBook"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
        self.__qualname__ = "PrintBook"

class Library:
    def __init__(self) -> None:
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        
        for book in self.books:
            #print(book.__qualname__)
            match book.__class__.__name__:
                case "Book":
                    print(f"Book: {book.title} by {book.author}")

                case "EBook":
                    print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}")

                case "PrintBook":
                    print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
                