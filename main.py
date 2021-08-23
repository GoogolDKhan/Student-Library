class Library:

    # Constructor
    def __init__(self, list_of_books):
        self.books = list_of_books

    # Method to display the books available in the library
    def display_available_books(self):
        print("Books available in this library are: ")
        for index, book in enumerate(self.books):
            print(f"{index+1}. {book}")

    # Method to borrow a book from the library
    def borrow_book(self, book_name):
        if book_name in self.books:
            print(
                f"You have been issued {book_name}. Please keep it safe and return it within 30 days"
            )
            self.books.remove(book_name)
            return True
        else:
            print(
                "Sorry. This book is either not available or has already been issued to someone else."
            )
            return False

    # Method to return a book from the student to library
    def return_book(self, book_name):
        self.books.append(book_name)
        print(
            "Thanks for returning this book! Hope you enjoyed reading this book. Have a great day ahead!"
        )


class Student:

    # Method to request a book from the library
    def request_book(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    # Method to return the borrowed book back to the library
    def return_book(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":

    # Book available in thw Central Library
    central_library = Library(
        [
            "Material Science",
            "Mechanics of Solids",
            "Fluid Mechanics",
            "Dynamics of Machines",
            "Manufacturing Process",
            "Heat Transfer",
        ]
    )

    student = Student()
    while True:
        welcome_message = """
        =====Welcome to Central Library=====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add or Return a book
        4. Exit the library
        """
        print(welcome_message)
        choice = int(input("Enter a choice: "))
        if choice == 1:
            central_library.display_available_books()
        elif choice == 2:
            central_library.borrow_book(student.request_book())
        elif choice == 3:
            central_library.return_book(student.return_book())
        elif choice == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            break
        else:
            print("Invalid Choice!")
