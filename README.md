# Bookshop Management Application

## Overview
The **Bookshop Management Application** is a command-line interface (CLI) tool designed to manage books, authors, and genres within a SQLite database. It is a practical solution for small bookstores or individuals looking to maintain an organized record of their book collection.

---

## Features
- **Add a Book**: Add a new book with its title, author, and genre.
- **Update a Book**: Modify the title of an existing book.
- **Delete a Book**: Remove a book record from the database.
- **List All Books**: Display all books along with their authors and genres.
- **Find Author by Book**: Retrieve the author of a specific book.
- **List All Genres**: View all available genres in the database.
- **Search Books by Author or Genre**: Use simple search algorithms to filter books by author or genre.
- **Algorithms for Sorting**: Sort books alphabetically or by genre for easier management.

---

## Technologies Used
- **Python**: Core programming language.
- **SQLAlchemy**: ORM (Object-Relational Mapping) for database interactions.
- **SQLite**: Lightweight, local database for storing data.
- **Pipenv**: Virtual environment and dependency management.

---

## Project Structure
```
project_root/
│
├── database_setup.py      # Database configuration and session setup.
├── functions.py          # Contains all business logic for CRUD operations.
├── models.py             # Defines the Author, Book, and Genre models.
├── xmain.py               # CLI interface for interacting with the application.
├── Pipfile               # Pipenv configuration for managing dependencies.
├── Pipfile.lock          # Lockfile for ensuring reproducible environments.
└── README.md             # Project documentation.
```

---

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Pipenv

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd bookshop-management
   ```

2. Set up the virtual environment and install dependencies:
   ```bash
   pipenv install
   pipenv shell
   ```

3. Initialize the database:
   ```bash
   python database_setup.py
   ```

4. Run the application:
   ```bash
   python main.py
   ```

---

## How to Use

### Menu Options
1. **Add a Book**:
   - Provide the book title, author name, and genre.
2. **Update a Book**:
   - Enter the book ID and the new title.
3. **Delete a Book**:
   - Enter the book ID to remove it from the database.
4. **List All Books**:
   - Displays a list of all books with their authors and genres.
5. **Find Author by Book**:
   - Input a book title to retrieve its author's name.
6. **List All Genres**:
   - Displays all genres available in the database.
7. **Search Books by Author or Genre**:
   - Filter books based on the author or genre to quickly find relevant results.
8. **Sort Books Alphabetically**:
   - Organize book listings alphabetically for easier browsing.
9. **Exit**:
   - Close the application.

---

## Example Usage
### Adding a Book
```bash
Enter your choice: 1
Enter book title: To Kill a Mockingbird
Enter author name: Harper Lee
Enter genre: Fiction
Book 'To Kill a Mockingbird' by Harper Lee in genre 'Fiction' added successfully.
```

### Listing All Books
```bash
Enter your choice: 4
ID: 1, Title: To Kill a Mockingbird, Author: Harper Lee, Genre: Fiction
```

### Searching Books
```bash
Enter your choice: 7
Search by (author/genre): author
Enter author name: Harper Lee
Books by Harper Lee:
- To Kill a Mockingbird (Fiction)
```

### Sorting Books Alphabetically
```bash
Enter your choice: 8
Books sorted alphabetically:
- Pride and Prejudice by Jane Austen (Romance)
- To Kill a Mockingbird by Harper Lee (Fiction)
```

---

## Enhancements
Future improvements could include:
- Adding user authentication for access control.
- Implementing additional tables, such as publishers or customer records.
- Enhancing the interface with a GUI.
- Adding algorithms for advanced data retrieval and sorting.

---

## License
This project is open-source and available under the MIT License.

---

## Contributing
Feel free to fork the repository and submit pull requests for any improvements or bug fixes. For major changes, please open an issue first to discuss what you would like to change.

---

## Contact
For questions or feedback, please reach out to [Your Email/Contact Information].

