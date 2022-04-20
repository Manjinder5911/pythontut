class Library:
    def __init__(self,list_books,library_name):
        self.list_books = list_books
        self.dict = {}
        self.given_book = []

    def displaybook(self):
        return f"The books are {self.list_books}"

    def lend_books(self):
        user_name = input("enter your name : \n")
        lend_book = input("enter the book name : \n")

        if lend_book in self.list_books:
            self.given_book.append(lend_book)
            self.list_books.remove(lend_book)
            self.dict.update({lend_book:user_name})
            return f"book lend successfully "
        elif lend_book in self.given_book:
            return f"book is unavailable and currently owned by {self.dict[lend_book]}"

    def add_book(self,) :
        print("write book name to be added")
        new_book = input("")
        self.list_books.append(new_book)
        return f"book added successfully"

    def return_book(self):
        returner_name = input("enter your name : \n")
        returned_book = input("enter book name : \n")
        if returned_book in self.given_book:
            self.list_books.append(returned_book)
            self.given_book.remove(returned_book)
            del self.dict[returned_book]
            return f"book returned successfully and {self.dict}"
        else:
            return f"enter valid book name"

if __name__ == '__main__':
    harry = Library(["a", "b", "c"], "harry_library")
    while True:
        user_input = input("enter 1 to display all books,2 to lend book,3 to add book, 4 to return book : \n")
        if user_input == '1':
            print(harry.displaybook())
        elif user_input == "2":
            print(harry.lend_books())

        elif user_input == "3":
            print(harry.add_book())
        elif user_input == "4":
            print(harry.return_book())
        else:
            print("enter valid input")

