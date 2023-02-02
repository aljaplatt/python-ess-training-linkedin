
#! try and read a non-existant file

# with open("a_file.txt") as file:
#     file.read()

# Traceback (most recent call last):
#   File "/Users/alexplatt/Desktop/projects/python-ess-training-linkedin/100-days/day-30/01.py", line 4, in <module>
    # with open("a_file.txt") as file: 

#? KeyError

# a_dict = {"key":"value"}
# value = a_dict["non_existant_key"]

# Traceback (most recent call last):
#   File "/Users/alexplatt/Desktop/projects/python-ess-training-linkedin/100-days/day-30_err_handling/01.py", line 15, in <module>
#     value = a_dict["non_existant_key"]
#             ~~~~~~^^^^^^^^^^^^^^^^^^^^
# KeyError: 'non_existant_key'

#? indexError

# fruit_list = ['apple', 'kiwi', 'cherry']
# fruit = fruit_list[3]

# Traceback (most recent call last):
#   File "/Users/alexplatt/Desktop/projects/python-ess-training-linkedin/100-days/day-30_err_handling/01.py", line 25, in <module>
#     fruit = fruit_list[3]
#             ~~~~~~~~~~^^^
# IndexError: list index out of range

#? TypeError

# text = 'abc'
# print(text + 5)

# Traceback (most recent call last):
#   File "/Users/alexplatt/Desktop/projects/python-ess-training-linkedin/100-days/day-30_err_handling/01.py", line 36, in <module>
#     print(text + 5)
#           ~~~~~^~~
# TypeError: can only concatenate str (not "int") to str


# FileNotFound
# try:
#     file = open("a_file.txt")
#! except:
#     # print("There was an error")
#     #* print is pointless, instead open in write mode
#     file = open("a_file.txt", "w")
#     #? this will look for the file, but create if doesnt exist
#     file.write("something")

#! problem above: According to PEP 8 - DO NOT USE BARE EXCEPT CLAUSE

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["zszszs"]) # this line should give a key error
#     #! line 60 fails and creates an exception, executing the except clause code - we dont know what is causing the exception!
# except:
#     file = open("a_file.txt", "w")
#     file.write("someting")

try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    # print(a_dictionary["zszszs"]) # this line should give a key error
    print(a_dictionary["key"]) # this line should give a key error
    #? we want more info, we want to catch a specific KeyError
except FileNotFoundError as e:
    print(f"file {e} doesnt exist")
    print(e)
    file = open("a_file.txt", "w")
    file.write("someting in file")
except KeyError as e:
    print(e)
    print("key doesnt exist")
    print(f"{e} doesnt exist")
#     Traceback (most recent call last):
#   File "/Users/alexplatt/Desktop/projects/python-ess-training-linkedin/100-days/day-30_err_handling/01.py", line 69, in <module>
#     print(a_dictionary["zszszs"]) # this line should give a key error
#           ~~~~~~~~~~~~^^^^^^^^^^
# KeyError: 'zszszs'
#? else block will run if no exceptions - the try block did not fail
else:
    content = file.read()
    print(content)
# finally not always needed but can be useful if you want something to execute regardless of outcome
finally:
    file.close()
    print("file closed")