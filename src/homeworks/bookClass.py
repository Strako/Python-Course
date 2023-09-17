import json 
import random

class Book:
    def __init__(self, title, author, editorial, isbn, quantity):
        self.title = title
        self.author = author
        self.editorial = editorial
        self.isbn = isbn
        self.quantity = quantity

    def __str__(self):
        return (
            f" Title: {self.title} \n Author: {self.author} \n Editorial: {self.editorial} \n" 
            f" ISBN: {self.isbn} \n Quantity: {self.quantity} \n"
        )
    
    def getBook(self):
        jsonString = json.dumps(self.__dict__, ensure_ascii=False)
        print(jsonString)
    
    def borrowBook(self):
        if(self.quantity > 0):
            self.quantity -= 1
        else:
            print("Theres no available books to borrow \n")
    
    def returnBook(self):
        self.quantity =+ 1
        
def main():
    book1 = Book("FLuyan mis lágrimas, dijo el policía", "Philp K. Dick", "minotauro", "978-607-07-4432-7", random.randint(0,100))
    book2 = Book("Fundación e Imperio", "Isaac Asimov", "Origen - Planeta", "968-22-0074-1",  0)

    print(book1)
    book1.borrowBook()

    print(book2)
    book2.borrowBook()

    book1.getBook()
    book2.getBook()

if __name__ == "__main__":
    main()


    