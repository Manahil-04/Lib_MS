# Library Management System

This is a Python library management system that allows you to manage a library's book collection, track members, and record book transactions. You can add books, check out books to library members, return books, and view the status of books in the library. This system also provides the ability to save and load library data to and from a CSV file for data persistence.

## Table of Contents
- [Setup](#setup)
- [Usage](#usage)
- [Class Overview](#class-overview)
- [CSV Data Storage](#csv-data-storage)

## Setup
1. Ensure you have Python installed on your system.
2. Download the code and save it to your desired directory.

## Usage

Before running the code, you can interact with the library management system by executing it in a Python environment. Here's how you can use the available functionality:

1. **Create a Library Object:**
   ```python
   library = Library()
   ```

2. **Add Books:**
   ```python
   library.add_book("Book Title", "Author Name")
   ```

3. **Display Books:**
   ```python
   library.display_books()
   ```

4. **Add Members:**
   ```python
   library.add_member("Member Name")
   ```

5. **Borrow a Book:**
   ```python
   library.borrow_book(member_id, book_id)
   ```

6. **Return a Book:**
   ```python
   library.return_book(member_id, book_id)
   ```

7. **Display Borrowed Books:**
   ```python
   library.display_borrowed_books()
   ```

## Class Overview

### LibraryMember

The `LibraryMember` class represents a library member with attributes such as `name`, `member_id`, and `books_issued`. It provides functionality to issue and return books, as well as display the books currently issued by the member.

### LibraryBook Class

The LibraryBook class is designed to represent individual books in the library. Each instance of this class contains information about a specific book, including its title and book ID. It also keeps track of whether the book is currently issued to a library member.

###Library

The `Library` class manages the library system. It keeps track of the library members, the available books, and the transactions. This class provides methods to add users, display users, save members to a CSV file, save transactions to a CSV file, and load members from a CSV file.

## CSV Data Storage

The system uses CSV files to persist data. The following CSV files are used:

- `books.csv`: Stores information about books, including their title, author, and the member to whom they are issued.

Make sure you have write permissions for the directory where the code is located to save data to CSV files.

**Note**: The system does not handle multiple simultaneous users, so make sure to run it in a single Python environment.

This is a simple library management system implemented in Python. It consists of two main classes: `LibraryMember` and `Library`, along with the necessary CSV file handling for data persistence.



### Functionality

- `add_user(name)`: Adds a new user to the library system with a unique member ID.
- `display_users()`: Displays the list of users in the library system.
- `save_members_to_csv()`: Saves the library members' data to a CSV file.
- `save_transactions_to_csv()`: Saves the transaction history to a CSV file.
- `load_members_from_csv()`: Loads the library members from a CSV file if it exists.

### CSV Files

The system uses CSV files for data persistence. The following files are used:

- `members.csv`: Contains data related to the library members.
- `transactions.csv`: Contains data related to the transactions performed in the library.

## Usage

You can use this library management system to manage users, books, and their transactions within a library. It provides basic functionalities for issuing and returning books, displaying user information, and persisting data to CSV files for future use.

Please ensure that you have the necessary CSV files (`members.csv` and `transactions.csv`) in the working directory for the system to function correctly.
