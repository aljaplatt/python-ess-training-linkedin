
print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm? '))

bill = 0

if height >= 120:
    print('ride')
    age = int(input('What is your age?'))
    if age < 12: 
        print('Free entry')
    elif age <= 18:
        print('Pay 5')
        bill = 5
    else: 
        print('Pay 8')
        bill = 8
    
    wants_photo = input('Photo? Y or N')
    if wants_photo == 'Y':
        bill += 3
    
    print(f'Your bill is {bill}')
else:
    print('come again') 