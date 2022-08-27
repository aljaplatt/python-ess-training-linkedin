piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

#* starts at first index, stops at second but doesn't include that num 
print(piano_tuple[1:2]) # 're'
print(piano_tuple[1:3]) # 're', mi
print(piano_tuple[2:3]) #  mi
print(piano_keys[2:3]) #  c

print(piano_tuple[1:]) # skips first num but returns eveything else 
print('11', piano_tuple[:len(piano_tuple) -1]) # misses last index

print(piano_keys[2:3:2]) #  every second item
print(piano_keys[::2]) #  every second item
print(piano_keys[::-1]) #  reverse list