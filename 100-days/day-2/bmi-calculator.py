# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
heightSq = float(height) * float(height)
result = float(weight) / heightSq
print(int(result))

bmi = int(weight) / float(height) **2
bmi_int = int(bmi)

