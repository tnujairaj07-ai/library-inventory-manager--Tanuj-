import json
import logging
from pathlib import Path
from .book import Book

class LibraryInventory:
    def __init__(self, json_path="books.json"):
        self.books = []
        self.json_path = Path(json_path)
        self.load_books()

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        logging.info(f"Added book: {title}")

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        if not self.books:
            return ""
        return "\n".join(str(book) for book in self.books)

    def issue_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book and book.issue():
            return True
        return False

    def return_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book and book.return_book():
            return True
        return False

    def save_books(self):
        try:
            with self.json_path.open('w', encoding='utf-8') as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)
            logging.info("Saved books to JSON.")
        except Exception as e:
            logging.error(f"Failed saving books: {e}")

    def load_books(self):
        if not self.json_path.exists():
            logging.warning("JSON file missing, starting with empty inventory.")
            return
        try:
            with self.json_path.open('r', encoding='utf-8') as f:
                data = json.load(f)
                self.books = [Book(**item) for item in data]
            logging.info("Loaded books from JSON.")
        except Exception as e:
            logging.error(f"Failed loading books: {e}")
            self.books = []
