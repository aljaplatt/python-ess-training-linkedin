student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {

}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    #* student will give us the key, to get the value, we must use student_scores[student]
    score = student_scores[student]
    if score > 90:
        #* check the score in student scores and assign appropriate grade to student grades dict.
        student_grades[student] = 'Outstanding'
    elif score > 80:
        student_grades[student] = 'Exceeds Expectations'
    elif score > 70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
    

# 🚨 Don't change the code below 👇
print(student_grades)