
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def check_out_book(self, title):
        """ [book._is_checked_out == True for book in self._books if book.title == title] """
        for book in self._books:
            if book.title == title:
                book.check_out()


    def return_book(self, title):
        """ [book._is_checked_out == False for book in self._books if book.title == title] """
        for book in self._books:
            if book.title == title: 
                book.return_book()

    def list_available_books(self):
        """ [print(book.__str__()) for book in self._books if book._is_checked_out == False] """
        for book in self._books:
            if book._is_checked_out == False:
                print(book.__str__())
