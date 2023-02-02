
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"]) 
#     #? we want more info, we want to catch a specific KeyError
# except FileNotFoundError as e:
#     print(e)
#     file = open("a_file.txt", "w")
#     file.write("someting in file")
# except KeyError as e:
#     print(f"{e} doesnt exist")
# #? else block will run if no exceptions - the try block did not fail
# else:
#     content = file.read()
#     print(content)
# # finally not always needed but can be useful if you want something to execute regardless of outcome
# finally:
#     raise KeyError("I made this error up - ")
#     # file.close()
#     # print("file closed")

#? When might you want to raise errors - unrealistic data?? 15 meters tall!!

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)