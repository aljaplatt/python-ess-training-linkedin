
#* __repr__
#? Customise an instance objects representation by implementing __repr__ in the objects class definition  

class Book:
    def __init__(self, title, author, book_type, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
    
    #? - representation - instance method - takes self
    #todo - alter how the instance is represented, eg: change obj to custom string.
    #* we can overwrite the default behaviour of repr in the class definition
    def __repr__(self):
        return f"The title is {self.title}"

hobbit = Book("The Hobbit", "Tolkein", "Paperback", 300)
lord_of_rings = Book("The Lord of the Rings", "Tolkein", "Hardback", 1300)

print(hobbit) #? The title is The Hobbit 
print(lord_of_rings) #? The title is The Lord of the Rings