from database_setup import session
from models import Author, Book, Genre

def add_book(title, author_name, genre_name):
    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
        session.add(author)
        session.commit()

    genre = session.query(Genre).filter_by(name=genre_name).first()
    if not genre:
        genre = Genre(name=genre_name)
        session.add(genre)
        session.commit()

    book = Book(title=title, author=author, genre=genre)
    session.add(book)
    session.commit()
    print(f"Book '{title}' by {author_name} in genre '{genre_name}' added successfully.")

def update_book(book_id, new_title):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        book.title = new_title
        session.commit()
        print(f"Book ID {book_id} updated to '{new_title}'.")
    else:
        print(f"Book ID {book_id} not found.")

def delete_book(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()
        print(f"Book ID {book_id} deleted successfully.")
    else:
        print(f"Book ID {book_id} not found.")

def list_books():
    books = session.query(Book).all()
    if books:
        for book in books:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author.name}, Genre: {book.genre.name}")
    else:
        print("No books found in the database.")

def find_author_by_book(title):
    book = session.query(Book).filter_by(title=title).first()
    if book:
        print(f"The author of '{title}' is {book.author.name}.")
    else:
        print(f"Book titled '{title}' not found.")

def list_genres():
    genres = session.query(Genre).all()
    if genres:
        print("Genres available:")
        for genre in genres:
            print(f"- {genre.name}")
    else:
        print("No genres found in the database.")

def search_books_by_author_or_genre(search_by, search_value):
    if search_by == "author":
        books = session.query(Book).join(Author).filter(Author.name.ilike(f"%{search_value}%")).all()
    elif search_by == "genre":
        books = session.query(Book).join(Genre).filter(Genre.name.ilike(f"%{search_value}%")).all()
    else:
        print("Invalid search criteria. Use 'author' or 'genre'.")
        return

    if books:
        print(f"Books found ({search_by}: {search_value}):")
        for book in books:
            print(f"- {book.title} by {book.author.name} ({book.genre.name})")
    else:
        print(f"No books found for {search_by} '{search_value}'.")

def sort_books():
    books = session.query(Book).order_by(Book.title).all()
    if books:
        print("Books sorted alphabetically:")
        for book in books:
            print(f"- {book.title} by {book.author.name} ({book.genre.name})")
    else:
        print("No books available to sort.")