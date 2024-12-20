import logging

logging.basicConfig(level=logging.WARNING) 
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

from functions import (
    add_book, update_book, delete_book, list_books, find_author_by_book, 
    list_genres, search_books_by_author_or_genre, sort_books
)

def main():
    while True:
        print("\nBookshop Management Application")
        print("1. Add a Book")
        print("2. Update a Book")
        print("3. Delete a Book")
        print("4. List All Books")
        print("5. Find Author by Book")
        print("6. List All Genres")
        print("7. Search Books by Author or Genre")
        print("8. Sort Books Alphabetically")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            genre = input("Enter genre: ")
            add_book(title, author, genre)
        elif choice == '2':
            book_id = int(input("Enter book ID to update: "))
            new_title = input("Enter new book title: ")
            update_book(book_id, new_title)
        elif choice == '3':
            book_id = int(input("Enter book ID to delete: "))
            delete_book(book_id)
        elif choice == '4':
            list_books()
        elif choice == '5':
            title = input("Enter book title to find the author: ")
            find_author_by_book(title)
        elif choice == '6':
            list_genres()
        elif choice == '7':
            search_by = input("Search by (author/genre): ")
            search_value = input(f"Enter {search_by} name: ")
            search_books_by_author_or_genre(search_by, search_value)
        elif choice == '8':
            sort_books()
        elif choice == '9':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
