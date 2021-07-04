# Implement student library system using OOPs where students can borrow book from list of books.Create a seperate Library & student class.your program must be menu driven.You are free to choose methods & attributes of your choice to implement this functionality.

class Library:

    def __init__(self,listOfBooks):
        self.books = listOfBooks
        
        
    def displayAvailableBooks(self):
        print("Books present in this library are:")
        for book in self.books:
            print(" *"+ book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it Safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else.Please wait untill the book is available")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student:
    def requestBook(self):
        self.book = input('Enter the name of the book you want to Borrow : ')
        return self.book

    def returnBook(self):
        self.book = input('Enter the name of the book you want to Return : ')
        return self.book

if __name__=="__main__":
    centralLibrary = Library(['Algorithm','Django','Data Structure','Python Notes'])
    student = Student()
    #centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n ~~~~~~~ Welcome to Central Library ~~~~~~~
        Please choose an Option:
        1. List all the Books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input('Enter a choice: '))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
        


