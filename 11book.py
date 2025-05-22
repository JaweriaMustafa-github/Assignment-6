# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count 
# when a new book is added.

class Book:
    total_books = 0 # Class variable to track total number of books

    def __init__(self, title):
        self.title = title
        Book.increment_book_count() # Increment count when a new book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
            
        
    @classmethod
    def get_total_books(cls):
        return cls.total_books
        
#Creating a book instance
b1 = Book("Python basics")
b2 = Book("Data science 101")
b3 = Book("AI for beginners")

#Displaying total number of books
print("Total books added:", Book.get_total_books())
