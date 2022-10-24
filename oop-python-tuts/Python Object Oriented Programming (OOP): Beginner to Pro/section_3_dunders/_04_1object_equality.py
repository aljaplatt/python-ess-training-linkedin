
#! This does assume that other is  is of the at least the of the same class, which could be a problem. It could be a completely different class, that also has a title and author. We should therefore put checks in place
'''
def __eq__(self, other):
        return self.title == other.title and self.author == other.author
'''

class Book:
    def __init__(self, title, author, book_type, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
    
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"

    # there are other, more advanced ways to handle this but for the mean time...
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False  
        return self.title == other.title and self.author == other.author

    
hobbit = Book("The Hobbit", "Tolkein", "Paperback", 300)
hobbit_2 = Book("The Hobbit", "Tolkein", "Paperback", 300)