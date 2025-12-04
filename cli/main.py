import logging
from librarymanager.inventory import LibraryInventory

logging.basicConfig(
    level=logging.INFO,
    filename='app.log',
    filemode='a',
    format='%(levelname)s:%(message)s'
)

def menu():
    print("\n=== Library Inventory Manager ===")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    return choice

def main():
    inventory = LibraryInventory()

    while True:
        choice = menu()
        try:
            if choice == '1':
                title = input("Book Title: ").strip()
                author = input("Author: ").strip()
                isbn = input("ISBN: ").strip()
                if not title or not author or not isbn:
                    print("All fields are required.")
                    continue
                inventory.add_book(title, author, isbn)
                inventory.save_books()
                print("Book added.")
            elif choice == '2':
                isbn = input("ISBN to Issue: ").strip()
                if inventory.issue_book(isbn):
                    inventory.save_books()
                    print("Book issued.")
                else:
                    print("Book not found or already issued.")
            elif choice == '3':
                isbn = input("ISBN to Return: ").strip()
                if inventory.return_book(isbn):
                    inventory.save_books()
                    print("Book returned.")
                else:
                    print("Book not found or not issued.")
            elif choice == '4':
                output = inventory.display_all()
                if output:
                    print(output)
                else:
                    print("No books in inventory.")
            elif choice == '5':
                query = input("Search by Title or ISBN: ").strip()
                books_by_title = inventory.search_by_title(query)
                book_by_isbn = inventory.search_by_isbn(query)

                if books_by_title:
                    print("\nFound by Title:")
                    for b in books_by_title:
                        print(b)
                if book_by_isbn:
                    print("\nFound by ISBN:")
                    print(book_by_isbn)
                if not books_by_title and not book_by_isbn:
                    print("No books found.")
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please enter 1-6.")
        except Exception as e:
            logging.error(f"Error in menu operation: {e}")
            print("An error occurred. Please try again.")

if __name__ == "__main__":
    main()
