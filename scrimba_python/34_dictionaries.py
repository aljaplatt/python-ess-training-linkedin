print("{Dictionaries}")

movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}

print(movie)
print(movie['title'])

# print(movie['budget']) #! unknown error 
# print(movie.get('budget')) #? None
print(movie.get('budget','not found')) #? set default value to 'not found'


#* update dictionary 
 
movie['title'] = 'The Holy Grail'
print(movie.get('title'))
movie['budget'] = 250000
movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})

#! remove/delete from dictionary 
# del movie['year']
# pop is used more often
year = movie.pop('year')
print(year, "YEAR")

print(len(movie))

print(movie.keys()) #? ›dict_keys(['title','year','cast'])
print(movie.items()) #? ›dict_items([('title', 'Life of Brian'),('year', 1979),('cast', ['John', 'Eric', 'Michael', 'George', 'Terry'])])

#? Looping DICTS

for key in movie:
    print(key)

'''
title
year
cast
'''

for key, value in movie.items():
    print(key, value)

'''
title Life of Brian
year 1979
cast ['John', 'Eric', 'Michael', 'George', 'Terry']
'''