class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Publication Year: {self.publication_year}")

    def is_older(self, current_year):
        return self.publication_year < current_year - 10

class SpecialEditionBook(Book):
    def __init__(self, title, author, isbn, publication_year, edition_number, has_slipcase=False):
        super().__init__(title, author, isbn, publication_year)
        self.edition_number = edition_number
        self.has_slipcase = has_slipcase

    def display_details(self):
        super().display_details()
        print(f"Edition Number: {self.edition_number}")
        print(f"Has Slipcase: {'Yes' if self.has_slipcase else 'No'}")

# Creating instances of the Book and SpecialEditionBook classes
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "978-0345391803", 1979)
special_book = SpecialEditionBook("Pride and Prejudice", "Jane Austen", "978-0141439518", 1813, 2, True)

print("--- Book Details ---")
book1.display_details()
print(f"Is it older than 10 years (in 2025)? {book1.is_older(2025)}")

print("\n--- Special Edition Book Details ---")
special_book.display_details()
print(f"Is it older than 10 years (in 2025)? {special_book.is_older(2025)}")