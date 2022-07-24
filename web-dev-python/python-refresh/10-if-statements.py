number = 7
user_input = input("Enter 'y' if you'd like to play: ").lower()

# if user_input == 'y':
#     user_number = int(input('Guess our number: '))
#     if user_number == number:
#         print('Correct')
#     else:
#         print('Sorry, incorrect!')

if user_input in ('y', 'Y'):
    user_number = int(input('Guess our number: '))
    if user_number == number:
        print('Correct')
    elif number - number in (1, -1):
        print("You were off by one")
    else:
        print('Sorry, incorrect!')

if user_input in ('y', 'Y'):
    user_number = int(input('Guess our number: '))
    if user_number == number:
        print('Correct')
    elif abs(number - number) == 1:
        print("You were off by one")
    else:
        print('Sorry, incorrect!')