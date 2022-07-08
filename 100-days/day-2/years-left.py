# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - int(age)

age_days = years_left * 365
age_weeks = years_left * 52
age_months = years_left * 12

output = f'You have {age_days} days, {age_weeks} weeks, and {age_months} months left.'

print(output)