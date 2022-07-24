
#* check if something is in something 

friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends) #? True

# --

movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")

if user_movie not in movies_watched:
    movies_watched.add(user_movie)

print(user_movie, movies_watched)
# print(user_movie in movies_watched)

# The `in` keyword works in most sequences like lists, tuples, and sets.