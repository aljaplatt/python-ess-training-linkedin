print("{Dictionaries}")

movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}

print(movie)
print(movie['title'])

# print(movie['budget']) #! error 
# print(movie.get('budget')) #? None
print(movie.get('budget','not found')) #? Not found

movie['title'] = 'The Holy Grail'
print(movie.get('title'))
movie['budget'] = 250000
movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})

#! remove 
del movie['year']
year = movie.pop('year')

print(movie.keys()) #? ›dict_keys(['title','year','cast'])
print(movie.items()) #? ›dict_items([('title', 'Life of Brian'),('year', 1979),('cast', ['John', 'Eric', 'Michael', 'George', 'Terry'])])

#? Looping DICTS

movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
for key in movie:
    print(key)

'''
title
›year
›cast
'''

for key, value in movie.items():
    print(key, value)

'''
›title Life of Brian
›year 1979
›cast ['John', 'Eric', 'Michael', 'George', 'Terry']
'''