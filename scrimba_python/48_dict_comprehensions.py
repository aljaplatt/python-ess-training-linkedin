# Dictionary comprehensions
movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
"Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
year =[1971,1975,1979,1982,1983,2014]
names = ['John','Eric','Michael','Graham','Terry','TerryG']

# print(list(zip(movies, year)))
'''
[('And Now for Something Completely Different', 1971), ('Monty Python and the Holy Grail', 1975), ("Monty Python's Life of Brian", 1979), ('Monty Python Live at the Hollywood Bowl', 1982), ("Monty Python's The Meaning of Life", 1983), ('Monty Python Live (Mostly)', 2014)]
'''

# give me a dict('movies': year) for each movies, year in zip(movies, year)
#* using for loop and zip  
new_dict = dict()
for movie, yr in zip(movies,year):
    new_dict[movie] = yr
print(new_dict)

#* using comprehension to do the same thing  

# new_dict_0 = {movie:yr for movie,yr in zip(movies,year)}
# print(new_dict)

# {'And Now for Something Completely Different': 1971, 'Monty Python and the Holy Grail': 1975, "Monty Python's Life of Brian": 1979, 'Monty Python Live at the Hollywood Bowl': 1982, "Monty Python's The Meaning of Life": 1983, 'Monty Python Live (Mostly)': 2014}

#* we only want the movies before 1983 

new_dict_1 = {movie:yr for movie,yr in zip(movies,year) if yr < 1983}
print(new_dict_1)

# {'And Now for Something Completely Different': 1971, 'Monty Python and the Holy Grail': 1975, "Monty Python's Life of Brian": 1979, 'Monty Python Live at the Hollywood Bowl': 1982}


new_dict_2 = {movie:yr for movie,yr in zip(movies,year) if yr < 1983 and movie.startswith('Monty')}
print(new_dict_2)
# {'Monty Python and the Holy Grail': 1975, "Monty Python's Life of Brian": 1979, 'Monty Python Live at the Hollywood Bowl': 1982}


n1 =[(name,movie,yr) for name,movie,yr in zip(names,movies,year) if yr < 1981]
print(n1)

# [('John', 'And Now for Something Completely Different', 1971), ('Eric', 'Monty Python and the Holy Grail', 1975), ('Michael', "Monty Python's Life of Brian", 1979)]


