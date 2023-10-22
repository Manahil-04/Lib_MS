# Library Management System

This is a simple library management system implemented in Python. It consists of two main classes: `LibraryMember` and `Library`, along with the necessary CSV file handling for data persistence.

## LibraryMember

The `LibraryMember` class represents a library member with attributes such as `name`, `member_id`, and `books_issued`. It provides functionality to issue and return books, as well as display the books currently issued by the member.

## Library

The `Library` class manages the library system. It keeps track of the library members, the available books, and the transactions. This class provides methods to add users, display users, save members to a CSV file, save transactions to a CSV file, and load members from a CSV file.

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

<<<<<<< HEAD
Please ensure that you have the necessary CSV files (`members.csv` and `transactions.csv`) in the working directory for the system to function correctly.
=======
Please ensure that you have the necessary CSV files (`members.csv` and `transactions.csv`) in the working directory for the system to function correctly.
>>>>>>> 5447ffc5049e595357f2c19935871d96903685b7
