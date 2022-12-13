
#? Dictionary comprehension

# new_dict = {new_key:new_value for item in list}
#* new dictionary based on values of an existing dictionary 
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
import random
names = ["Alex", "Kelly", "Alan", "Jen", "Bruce", "Clark", "Diana"]

students_scores = {name:random.randint(1,100) for name in names}

print("SS: ", students_scores) 
# SS:  {'Alex': 27, 'Kelly': 95, 'Alan': 58, 'Jen': 100, 'Bruce': 58, 'Clark': 22, 'Diana': 89}

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print("PS: ", passed_students)
# PS:  {'Kelly': 95, 'Jen': 100, 'Diana': 89}


#* ex 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

word_list = sentence.split()
# print("WL: ", word_list)
# Write your code below:

result = {word:len(word) for word in word_list}

print("RES: ", result)

#* ex 2

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
# {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}
print(weather_f) 

# loop through a dictionary 

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,99,23]
}

for (key, value) in student_dict.items():
    print(key)
    print(value)
# student
# ['Angela', 'James', 'Lily']
# score
# [56, 99, 23]

import pandas as pd # pip install pandas

student_dataframe = pd.DataFrame(student_dict)
print("PD: ", student_dataframe)

# PD: student  score
# 0  Angela     56
# 1   James     99
# 2    Lily     23

# Loop through dataframe - but this output is not so useful

for (key, value) in student_dataframe.items():
    print(key)
    print(value)

# better to use iterrows

for (index, row) in student_dataframe.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
    if row.student == "Lily":
        print(row.score)
