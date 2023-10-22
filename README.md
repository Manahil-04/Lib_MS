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

### `LibraryBook`
- Represents a book in the library.
- Attributes:
  - `title`: The title of the book.
  - `author`: The author of the book.
  - `book_id`: A unique identifier for the book.
  - `issued_to`: The library member to whom the book is currently issued.

### `Library`
- Manages the library's books and members.
- Methods:
  - `add_book(title, author)`: Add a new book to the library.
  - `display_books()`: Display a list of all books in the library.
  - `borrow_book(member_id, book_id)`: Allow a library member to borrow a book.
  - `return_book(member_id, book_id)`: Record the return of a book by a member.
  - `display_borrowed_books()`: Display a list of borrowed books and the members who have them.
  - `save_books_to_csv()`: Save the library's book data to a CSV file.
  - `load_books_from_csv()`: Load book data from a CSV file.

## CSV Data Storage

The system uses CSV files to persist data. The following CSV files are used:

- `books.csv`: Stores information about books, including their title, author, and the member to whom they are issued.

Make sure you have write permissions for the directory where the code is located to save data to CSV files.

**Note**: The system does not handle multiple simultaneous users, so make sure to run it in a single Python environment.

Feel free to modify and extend this library management system to suit your specific needs or integrate it into a larger application.