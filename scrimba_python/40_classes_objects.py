print("Classes & Objects")

#Classes are blueprints
#Objects are the actual things you built
#variables => attributes
#functions => methods

class Movie:
    def __init__(self, title, year, imdb, have_seen):
        self.title = title
        self.year = year
        self.imdb = imdb
        self.have_seen = have_seen
    
    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb)
        print("I have seen it: ", self.have_seen)
    
film_1 = Movie("Life of Brian",1979,8.1,True)
film_2 = Movie("The Holy Grail",1975,8.2,True)

# print(film_1.title, film_1.imdb)
# print(film_1['title'], film_1['imdb']) #! ERR

film_2.nice_print()
#* no parameter as self acts as a reference to the object its being called on - film_2
# same as calling - Movie.nice_print(film_2) 

films = [film_1,film_2]
print(films[1].title,films[0].title)
films[0].nice_print()