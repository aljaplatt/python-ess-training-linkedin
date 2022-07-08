
#* If the bill was $150.00, split between 5 people, with 12% tip  
#? Each person should pay 
print('Welcome to the tip calculator')
total_bill = input('What was the total bill? £ \n')
tip_amount = input('What size tip? 10, 12 or 15? \n')
num_people = input('How many people will split the bill? \n')

tip_percentage = float(f'1.{tip_amount}')
# bill_pp = round((int(total_bill) * tip_percentage) / int(num_people), 2)
bill_pp = (int(total_bill) * tip_percentage) / int(num_people)
final_amount = "{:.2f}".format(bill_pp)
print(final_amount)
# print(f'Each person should pay: £{round(bill_pp, 3)}')

# print(round(bill_tip, 2))
# print(total_bill, tip_amount,num_people)