# ── BOOK CLASS ─────────────────────────────────────────────────
# TODO: Define a class called Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    # TODO: Define __init__(self, title, author)
    #   Set up three attributes:
    #     self.title   = title
    #     self.author  = author
    #     self.is_borrowed = False   ← starts as not borrowed
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    # TODO: Define borrow(self)
    #   If self.is_borrowed is already True → print that it's already borrowed
    #   Otherwise → set self.is_borrowed = True and print a borrow message
    def borrow(self):
        if self.is_borrowed:
            print(self.title, "is already borrowed.")
        else:
            self.is_borrowed = True
            print(self.title, "has been borrowed.")

    # TODO: Define return_book(self)
    #   If self.is_borrowed is False → print that it wasn't borrowed
    #   Otherwise → set self.is_borrowed = False and print a return message
    def return_book(self):
        if not self.is_borrowed:
            print(self.title, "was not borrowed.")
        else:
            self.is_borrowed = False
            print(self.title, "has been returned.")

    # TODO: Define __str__(self)
    #   Return a string like:  "Title by Author [Available]"
    #   or                     "Title by Author [Borrowed]"
    def __str__(self):
        return "Title by author [Available]"
    


# ── LIBRARY ────────────────────────────────────────────────────
# TODO: Create at least 3 Book objects with different titles and authors
# Example: book1 = Book("Python Crash Course", "Eric Matthes")

book1=Book("Sherlock Holmes", "Arthur Conan Doyle")
book2=Book("Wings Of Fire", "T.U.I T Sutherland")
book3=Book("When the mountain meets the moon", "Grace Lin")

# TODO: Print each book (uses __str__ automatically)
print(book1)
print(book2)
print(book3)

# TODO: Borrow some books using .borrow()
# TODO: Try to borrow the same book twice to test the guard message
book1.borrow()
book2.borrow()
book3.borrow()

# TODO: Return a book using .return_book()
# TODO: Try to return a book that was never borrowed to test that guard
book1.return_book()
book2.return_book()
book3.return_book()

# TODO: Print each book again to show updated status
print(book1)
print(book2)
print(book3)