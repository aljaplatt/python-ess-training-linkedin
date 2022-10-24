
#* dunder format allows you to customise how our own instance objects will be string formatted

# print(type(f"{100}")) # int -> <class '
# print(format(100, ".3f")) # 100.000
# print("{:.3f}".format(100)) # 100.000

class Book:
    def __init__(self, title, author, book_type, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
    
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"

    #? an instance method, but also takes a second argument 
    def __format__(self, format_spec):
        if format_spec == "short":
            return f"{self.title} - {self.author}"
        elif format_spec == "pages":
            return f"{self.pages}"
        # if not short return repr
        return repr(self)


hobbit = Book("The Hobbit", "Tolkein", "Paperback", 300)
lord_of_rings = Book("The Lord of the Rings", "Tolkein", "Hardback", 1300)

# full repr 
print(f"{hobbit}") # Book('The Hobbit', 'Tolkein', 'Paperback', '300')

print(f"{hobbit:short}") # The Hobbit - Tolkein
print(f"{hobbit:pages}") # 300

print("{}".format(hobbit)) # Book('The Hobbit', 'Tolkein', 'Paperback', '300')
print("{:short}".format(hobbit)) # The Hobbit - Tolkein
