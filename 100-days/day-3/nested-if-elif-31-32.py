#? Nested

# if condition:
#     if another_condition:
#         do this
#     else:
#         do this
# else:
#     do this

print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm? '))

# if height >= 120:
#     print('ride')
#     age = int(input('What is your age?'))
#     if age <= 18:
#         print('Pay sweets')
#     else: 
#         print('Pay gold')
# else:
#     print('come again') 


#* More conditions? elif  - else if 

if height >= 120:
    print('ride')
    age = int(input('What is your age?'))
    if age < 12: 
        print('Free entry')
    elif age <= 18:
        print('Pay sweets')
    else: 
        print('Pay gold')
else:
    print('come again') 


#* BMI 

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

bmi = round(weight / height **2)

if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are underweight.')
elif bmi < 25:
    print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi < 30:
    print(f'Your BMI is {bmi}, you are overweight.')
elif bmi < 35:
    print(f'Your BMI is {bmi}, you are obese.')
else:
    print(f'Your BMI is {bmi}, you are clinically obese.')
    

