programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",
    
    }
# print(programming_dictionary)
# print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)

for value in programming_dictionary:
    print(value)
    print(programming_dictionary[value])