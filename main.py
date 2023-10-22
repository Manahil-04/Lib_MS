import csv

class LibraryBook:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.issued_to = None

    def issue(self, member):
        if self.issued_to is None:
            self.issued_to = member
            member.issue_book(self)
            print(f"Book '{self.title}' has been issued to {member.name}")
        else:
            print(f"Book '{self.title}' is already issued to {self.issued_to.name}")

    def return_book(self):
        if self.issued_to:
            print(f"Book '{self.title}' has been returned by {self.issued_to.name}")
            self.issued_to.return_book(self)
            self.issued_to = None
        else:
            print(f"Book '{self.title}' is not currently issued to anyone.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = [] 

    def add_book(self, title, author):
        book_id = len(self.books) + 1
        book = LibraryBook(title, author, book_id)
        self.books.append(book)
        print(f"Book added: {book.title}")
        self.save_books_to_csv() 

    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            print(book.title)

    def borrow_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if member and book:
            book.issue(member)
            self.transactions.append({"user": member, "book": book, "action": "borrow"})
            print(f"{member.name} borrowed {book.title}")
            self.save_transactions_to_csv() 
        else:
            print("Invalid user or book")

    def return_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if member and book:
            book.return_book()
            self.transactions.append({"user": member, "book": book, "action": "return"})
            self.save_transactions_to_csv()  # Save to CSV after a transaction
        else:
            print("Invalid user or book")

    def display_borrowed_books(self):
        borrowed_books = [book for book in self.books if book.issued_to is not None]
        if borrowed_books:
            print("Borrowed Books:")
            for book in borrowed_books:
                print(f"{book.title} (Issued to: {book.issued_to.name})")
        else:
            print("No books are currently borrowed.")


    def save_books_to_csv(self):
        with open('books.csv', 'w', newline='') as csvfile:
            fieldnames = ['book_id', 'title', 'author', 'issued_to']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for book in self.books:
                writer.writerow({
                    'book_id': book.book_id,
                    'title': book.title,
                    'author': book.author,
                    'issued_to': book.issued_to.name if book.issued_to else ''
                })

    def load_books_from_csv(self):
        try:
            with open('books.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    book = LibraryBook(row['title'], row['author'], int(row['book_id']))
                    if row['issued_to']:
                        member = next((m for m in self.members if m.name == row['issued_to']), None)
                        book.issue(member)
                    self.books.append(book)
        except FileNotFoundError:
            pass  