# 🚨 Don't change the code below 👇
from cgitb import reset


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
total = 0
count = 0
for height in student_heights:
    total += height
    count += 1
   
result = round(total / count)
print(result)

# * method without for loop

total_height = sum(student_heights)
num_students = len(student_heights)
avr_height = round(total_height / num_students)
print(avr_height)


