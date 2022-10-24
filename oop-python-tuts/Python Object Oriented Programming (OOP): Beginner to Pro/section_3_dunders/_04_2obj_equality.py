
# ? - in the previous files we described what equality should look like using the __eq__ 'magic' method. But by doing this we also defined what conditions define non-equality.

#* However we can also control this behaviour using __ne__ 

class Book:
    def __init__(self, title, author, book_type, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
    
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"


    def __eq__(self, other):
        if not isinstance(other, Book):
            return False  
        return self.title == other.title and self.author == other.author

    def __ne__(self, other):
        print("Comparing non equality")

    
hobbit = Book("The Hobbit", "Tolkein", "Paperback", 300)
hobbit_2 = Book("The Hobbit", "Tolkein", "Paperback", 300)