
#* Both dunder str and repr are used to define custom string representations for a given object
#? repr should ideally return valid python code which, if evaluated, rebuilds the instance.   
#* - opinion - if you don't have a strong reason to define str, don't bother. __repr__ alone is fine.

class Book:
    def __init__(self, title, author, book_type, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
    
    
    def __repr__(self):
        #? one way... but it wouldn't allow us to directly reconstruct the instance
        #* return f"Attributes: title: {self.title}, author: {self.author}, book_type: {self.book_type} and pages: {self.pages}"
        #todo - but a better way would allow us to return a string that we could pass to eval to reconstruct the instance
        # eval() evaluates strings as if they were python expressions eval("2+2") returns 4
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"
    

    # def __str__(self):
    #     return f"{self.title} by {self.author} in {self.book_type}"

hobbit = Book("The Hobbit", "Tolkein", "Paperback", 300)
lord_of_rings = Book("The Lord of the Rings", "Tolkein", "Hardback", 1300)

#todo - changes the 'string' representation of the instance, what is returned when we pass the instance object 
# print("STR REP: ",str(hobbit))
#? The Hobbit by Tolkein in Paperback 
#* However, now if we just print the instance...
# print("JUST PRINT: ", hobbit) 
#todo - We get... The Hobbit by Tolkein in Paperback, which has changed. 

#? However the object representation has not changed... 
# print("REPR: ", repr(hobbit))
#? The title is The Hobbit - default representation for the object.


#? Why do we need both of these methods ??? 

#* __str__ is intended to return an informal string representation to an end user

#! __repr__ is intended to give the developer, or users of the class, an indication of how the instance can be replicated. More 'dev' oriented 
#* Our goal with __repr__ should be to return a string that describes an instance more fully. 
#? It should include all the details a developer would need to recreate the instance. 

# print(hobbit.__dict__)
'''
{
    'title': 'The Hobbit', 
    'author': 'Tolkein', 
    'book_type': 'Paperback', 
    'pages': 300
}
'''
#* Our repr should be disclosing all of these properties.

#?  first way returns - REPR:  Attributes: title: The Hobbit, author: Tolkein, book_type: Paperback and pages: 300 

#* BEST WAY returns an object that we can directly recreate the instance - 
print("z: ", repr(hobbit)) 
#todo-  Book('The Hobbit', 'Tolkein', 'Paperback', '300') 
#* with this we can use eval() - we can show how the instance was created.
print(eval(repr(hobbit))) # Book('The Hobbit', 'Tolkein', 'Paperback', '300')

#? DO WE ALWAYS NEED BOTH REPR AND STR ??? 
# Maybe - but not necessarily - if only one pick __repr__
