books = [
    {
        "book_id": 101,
        "title": "Python Programming",
        "author": "Guido van Rossum",
        "category": "Programming",
        "copies": 5
    },
    {
        "book_id": 102,
        "title": "Machine Learning",
        "author": "Tom Mitchell",
        "category": "Artificial Intelligence",
        "copies": 3
    },
    {
        "book_id": 103,
        "title": "Deep Learning",
        "author": "Ian Goodfellow",
        "category": "Artificial Intelligence",
        "copies": 4
    }
]

def book_info(book):

    print("-" * 70)
    print(f"Book ID       : {book['book_id']}")
    print(f"Title         : {book['title']}")
    print(f"Author        : {book['author']}")
    print(f"Category      : {book['category']}")
    print(f"No. of Copies : {book['copies']}")
    print("-" * 70)

#book_info(books[0])

def add_book():

    book_id = int(input("Enter Book ID: "))
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    category = input("Enter Book Category: ")
    copies = int(input("Enter Number of Copies: "))

    new_book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "copies": copies
    }

    # Check if book already exists
    for book in books:
        if book["book_id"] == book_id:
            book["copies"] += copies
            print("-" * 70)
            print("✅ Book already exists.")
            print(f"Copies updated successfully! Total Copies: {book['copies']}")
            print("-" * 70)
            return

    books.append(new_book)

    print("-" * 70)
    print("✅ Book added successfully!")
    print("-" * 70)

#add_book()

def display_book():

    if not books:
        print("-" * 70)
        print("❌ No books found!")
        print("-" * 70)
        return

    print("\n📚 Library Books\n")

    for book in books:
        book_info(book)

#display_book()

def search_book():

    if not books:
        print("-" * 70)
        print("❌ No books found!")
        print("-" * 70)
        return

    book_id = int(input("Enter Book ID to search: "))

    for book in books:

        if book["book_id"] == book_id:

            print("\n📖 Book Found\n")
            book_info(book)
            return

    print("-" * 70)
    print("❌ Book ID not found!")
    print("-" * 70)

#search_book()

def update_book():

    if not books:
        print("-" * 70)
        print("❌ No books found!")
        print("-" * 70)
        return

    book_id = int(input("Enter Book ID to update: "))

    for book in books:

        if book["book_id"] == book_id:

            print("\nBefore Updating")
            book_info(book)

            book["title"] = input("Enter New Title: ")
            book["author"] = input("Enter New Author: ")
            book["category"] = input("Enter New Category: ")
            book["copies"] = int(input("Enter Number of Copies: "))

            print("\nAfter Updating")
            book_info(book)

            print("✅ Book updated successfully!")
            return

    print("-" * 70)
    print("❌ Book ID not found!")
    print("-" * 70)

#update_book()

def delete_book():

    if not books:
        print("-" * 70)
        print("❌ No books found!")
        print("-" * 70)
        return

    book_id = int(input("Enter Book ID to delete: "))

    for book in books:

        if book["book_id"] == book_id:

            print("\nBook Information")
            book_info(book)

            choice = input(
                "Are you sure you want to delete this book? (y/n): "
            ).lower()

            if choice in ["y", "yes"]:

                books.remove(book)

                print("-" * 70)
                print("✅ Book deleted successfully!")
                print("-" * 70)

            else:

                print("-" * 70)
                print("❌ Deletion cancelled!")
                print("-" * 70)

            return

    print("-" * 70)
    print("❌ Book ID not found!")
    print("-" * 70)

#delete_book()

def save_data(file="books.json"):

    with open(file, "w") as f:
        json.dump(books, f, indent=4)

    print("✅ Data saved successfully!")

#save_data()

def load_data(file="books.json"):

    global books

    try:

        with open(file, "r") as f:
            books = json.load(f)

        print("✅ Data loaded successfully!")

    except FileNotFoundError:

        books = []
        print("⚠️ No existing data found. Starting with an empty library.")

#load_data()

def system():

    load_data()

    while True:

        print("=" * 70)
        print("                 LIBRARY MANAGEMENT SYSTEM")
        print("=" * 70)

        print("\n1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Save Data")
        print("7. Exit\n")

        print("=" * 70)

        try:

            choice = int(input("Enter your choice (1-7): "))
            print("=" * 70)

            if choice == 1:
                add_book()

            elif choice == 2:
                display_book()

            elif choice == 3:
                search_book()

            elif choice == 4:
                update_book()

            elif choice == 5:
                delete_book()

            elif choice == 6:
                save_data()

            elif choice == 7:

                save_data()

                print("-" * 70)
                print("💖 Thank you for using Library Management System!")
                print("-" * 70)

                break

            else:
                print("❌ Please enter a number between 1 and 7.")

        except ValueError:
            print("-" * 70)
            print("❌ Invalid input! Please enter a valid number.")
            print("-" * 70)

if __name__ == "__main__":
    system()
