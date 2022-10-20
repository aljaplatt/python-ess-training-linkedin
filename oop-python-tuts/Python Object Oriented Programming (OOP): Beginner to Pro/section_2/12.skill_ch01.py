from random import choice

class Student:
    educational_platform = "Udemy"

    def __init__(self, name, age=16):
        self.name = name
        self.age = age
    
    def greet(self):
        # https://www.w3schools.com/python/ref_string_format.asp
        _greetings = ['Hey, {}', "Hi, {}", 'Hey there, {}', 'Hello, {}', 'Wassup yo, {}']
        # return f'{choice(_greetings)} my name is {self.name}'
        greeting = choice(_greetings)
        return greeting.format(self.name)

# s1 = Student("Alex")
# students = [
#     Student("Alex"), 
#     Student("Alan"), 
#     Student("Kelly"), 
#     Student("Kalem"), 
#     Student("Jenny")
#     ]
# # print(s1.greet())

# for student in students:
#     print(student.greet())



def class_create(student_names):
    return [Student(name) for name in student_names]

names = ["Alex", "Alan", "Kelly", "Kalem", "Jenny"]

for student in class_create(names):
    print(student.greet())