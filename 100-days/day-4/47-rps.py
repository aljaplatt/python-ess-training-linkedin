import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player_choice = int(input('"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."'))

cpu_choice = random_int = random.randint(0,2)
print(cpu_choice)
#* Is player input a number between 0-2 ?

if player_choice >= 0 and player_choice <= 2:
    if cpu_choice == 0:
        img = rock
    if cpu_choice == 1:
        img = paper
    if cpu_choice == 2:
        img = scissors
    if cpu_choice == player_choice:
        print('Draw')
    elif cpu_choice == 0 and player_choice == 2 or cpu_choice == 1 and player_choice == 0 or cpu_choice == 2 and player_choice == 1:

        print(f'You lose! The computer chose {img}')
    else:
        print(f'You Win The computer chose {img}')
else:
    print('Invalid number')


