
class Book:
    def __init__(self, title, author, book_type, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
    
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"

    #? __eq__ takes a second argument which represents the object this instance is being compared to.
    def __eq__(self, other):
        # here we're always returning True, makes no sense but illustrates that we can change behaviour
        # return True
        #! DUCK TYPING PROBLEM - SEE NEXT FILE 
        return self.title == other.title and self.author == other.author

    
hobbit = Book("The Hobbit", "Tolkein", "Paperback", 300)
hobbit_2 = Book("The Hobbit", "Tolkein", "Paperback", 300)
lord_of_rings = Book("The Lord of the Rings", "Tolkein", "Hardback", 1300)

#? without eq = False, with eq = True
print(hobbit == hobbit_2) # False - same content, different objects in memory
print(hobbit == lord_of_rings) # False



print(id(hobbit)) # 4343197184
print(id(hobbit_2)) # 4342959360

#* This is the default behaviour, but we can change what equality means if we need to, by defining __eq__ in our class. 



