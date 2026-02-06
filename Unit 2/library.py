#Library Class
class Library:
    def __init__(self, book_name, author, available=True):
        self.book_name =book_name
        self.author=author
        self.available=available
    def check_out(self):
        if self.available:
            self.available=False
            print(f'"{self.book_name}"has been checked out')
        else:
            print(f'"{self.book_name}"is currently not available')

    def return_book(self):
        self.available=True
        print(f'"{self.book_name}"has been returned and is not available')

    def display_book(self):
        status="Available"if self.available else "Not Available"
        print(f"Book Name: {self.book_name},Author: {self.author},Status: {self.status}")       
Book1 = Library("Python Programming","Guido van Rossum")
Book2= Library("Data structure","Marl Allen Weiss")

Book1.display_book()
Book1.check_out()
Book1.display_book()

Book1.return_book()
Book2.display_book()

