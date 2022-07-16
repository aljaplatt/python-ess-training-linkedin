import random
# 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
#* without choice
#! off by one err 
# list_length = len(names) - 1
# random_number= random.randint(0, list_length)
# random_name = names[random_number]
# print(f'{random_name} is going to buy the meal today!')

#* using random.choice()
# list_length = len(names) - 1
# random_number= random.randint(0, list_length)
random_name = random.choice(names)
print(f'{random_name} is going to buy the meal today!')
