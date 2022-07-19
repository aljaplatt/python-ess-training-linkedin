# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
namesLower  = name1.lower() + name2.lower()
# name2Lower = name2.lower()
t= namesLower.count('t')
r= namesLower.count('r')
u= namesLower.count('u')
e= namesLower.count('e')
true= t + r + u + e 
l= namesLower.count('l')
o= namesLower.count('o')
v= namesLower.count('v')
e= namesLower.count('e')
love = l + o + v + e 
love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f'Your love score is {love_score}, you go together like coke and mentos.')
elif love_score >= 40 and love_score <= 50:
    print(f'Your love score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}')





