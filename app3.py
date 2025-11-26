class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []  

    def addbook(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def searchbook(self, title):
        for book in self.books:
            if book.title == title:
                print("Book found!")
                print("Title:", book.title)
                print("Author:", book.author)
                return
        print("Book not found.")

    def display(self):
        if not self.books:
            print("No books available.")
            return
        print("\nAll Books:")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book.title} by {book.author}")




library = Library()
ch = 0
while ch != 4:
    print("\nMENU\n1. Add Book\n2. Search Book\n3. Display All Books\n4. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        t = input("Enter book title: ")
        a = input("Enter author name: ")
        book = Book(t, a)
        library.addbook(book)

    elif ch == 2:
        t = input("Enter title to search: ")
        library.searchbook(t)

    elif ch == 3:
        library.display()

    elif ch == 4:
        print("Exiting...")

    else:
        print("Invalid choice")
