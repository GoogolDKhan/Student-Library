class Library:

    # Constructor
    def __init__(self, listofBooks):
        self.books = listofBooks

    # Method to display the books available in the library
    def displayAvailableBooks(self):
        print("Books available in this library are: ")
        for index, book in enumerate(self.books):
            print(f"{index+1}. {book}")

    # Method to borrow a book from the library
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print(
                "Sorry. This book is either not available or has already been issued to someone else.")
            return False

    # Method to return a book from the student to library
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading this book. Have a great day ahead!")


class Student:

    # Method to request a book from the library
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    # Method to return the borrowed book back to the library
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":

    # Book available in thw Central Library
    centralLibrary = Library(['Material Science', 'Mechanics of Solids', 'Fluid Mechanics',
                             'Dynamics of Machines', 'Manufacturing Process', 'Heat Transfer'])

    student = Student()
    while(True):
        welcomeMsg = '''
        =====Welcome to Central Library=====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add or Return a book
        4. Exit the library
        '''
        print(welcomeMsg)
        choice = int(input("Enter a choice: "))
        if choice == 1:
            centralLibrary.displayAvailableBooks()
        elif choice == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif choice == 3:
            centralLibrary.returnBook(student.returnBook())
        elif choice == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            break
        else:
            print("Invalid Choice!")
