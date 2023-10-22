import csv

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books_issued = []

    def issue_book(self, book):
        self.books_issued.append(book)

    def return_book(self, book):
        if book in self.books_issued:
            self.books_issued.remove(book)
        else:
            print(f"Book '{book.title}' was not issued to {self.name}")

    def display_issued_books(self):
        print(f"{self.name} has the following books issued:")
        for book in self.books_issued:
            print(book.title)


class Library:
    def __init__(self):
        self.members = []
        self.books = []
        self.transactions = [] 


    def add_user(self, name):
        member_id = len(self.members) + 1
        member = LibraryMember(name, f"M{member_id:03d}")
        self.members.append(member)
        print(f"User added: {member.name}")
        self.save_members_to_csv()  # Save to CSV after adding a user


    def display_users(self):
        print("Users in the library:")
        for member in self.members:
            print(member.name)

    

    def save_members_to_csv(self):
        with open('members.csv', 'w', newline='') as csvfile:
            fieldnames = ['member_id', 'name', 'books_issued']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for member in self.members:
                writer.writerow({
                    'member_id': member.member_id,
                    'name': member.name,
                    'books_issued': ', '.join([book.title for book in member.books_issued])
                })

    def save_transactions_to_csv(self):
        with open('transactions.csv', 'w', newline='') as csvfile:
            fieldnames = ['user_id', 'book_id', 'action']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for transaction in self.transactions:
                writer.writerow({
                    'user_id': transaction['user'].member_id,
                    'book_id': transaction['book'].book_id,
                    'action': transaction['action']
                })

    def load_members_from_csv(self):
        try:
            with open('members.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    member = LibraryMember(row['name'], row['member_id'])
                    books_issued = row['books_issued'].split(', ')
                    for book_title in books_issued:
                        book = next((b for b in self.books if b.title == book_title), None)
                        member.issue_book(book)
                    self.members.append(member)
        except FileNotFoundError:
            pass 

