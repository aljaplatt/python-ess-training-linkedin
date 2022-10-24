
#* __repr__

class Book:
    def __init__(self, title, author, book_type, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages

book = Book("The Hobbit", "Tolkein", "Softback", 300)

print(book) # The is the same as the output from repr(book)
# The repr() function returns a printable representational string of the given object. https://www.programiz.com/python-programming/methods/built-in/repr
#? <__main__.Book object at 0x102bc2e30> 

#todo - This shows it is an instance of the class Book stored at the location 0x102bc2e30 in memory. This is not very useful.

#* This is not very useful 