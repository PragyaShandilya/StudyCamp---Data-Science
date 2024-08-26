'''1. Design a Library Management System
Requirements:
Implement classes for Book, Member, Librarian, and Library.
Book should have attributes like title, author, ISBN, and status.
Member should have attributes like name, member_id, and a list of borrowed books.
Librarian should have attributes like name and employee_id.
Library should have a collection of books and methods to add/remove books, register members, lend books, and return books.
'''
class Book:
    def __init__(self,title,author,ISBN,status):
        self.title = title
        self.author = author
        self.ISBN = ISBN 
        self.status = status
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("ISBN: ", self.ISBN)
        print("Status: ", self.status)

class Member:
    def __init__(self, name, memb_id, List):
        self.name = name
        self.memb_id = memb_id
        self.List = List
        print("Name of Member: ", self.name)
        print("Member ID: ", self.memb_id)
        print("Borrowed Books: ", self.List)
        
class Librarian:
    def __init__(self, name,emp_id):
        self.name = name
        self.emp_id = emp_id
        print("Name of Librarian: ", self.name)
        print("Employee ID: ", self.emp_id)

class Library:
    def __init__(self, All_Books, register_memb, lent, returned):
        self. All_Books = All_Books
        self.register_memb = register_memb
        self.lent = lent
        self.returned = returned
        print("All Books in Library are: ", self.All_Books)
        print("Registered Members are:\n", self.register_memb)
        print("Lent Books: ", self.lent)
        print("Returned Books: ",self.returned)

#-----------------------------------------------------------------------------------
Book1 = Book("ABC Murders", "Agatha Christie", 1234, "Available")
List_borrowed = ['Murder on Orient Express', 'Harry Potter and Sorcerer\'s Stone']
Member1 = Member("XYZ", 1003, List_borrowed)
Librarian1 = Librarian("PQR", 4567)
collection = ['Lord of the rings', 'Song of Ice and Fire', 'Murder on Orient Express', 'Harry Potter and Sorcerer\'s Stone', 'Harry Potter and chamber of Secrets']
memb = [Member1.name]
lent = ['Murder on Orient Express']
returned = ['Harry Potter and Sorcerer\'s Stone']
Library1 = Library(collection,memb,lent, returned)
