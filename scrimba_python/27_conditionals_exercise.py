# def num_days(month):

#     if month == 'jan':
#         print('number of days in',month,'is',31)
#     elif month == 'feb':
#         print('number of days in',month,'is',28)
#     elif month == 'mar':
#         print('number of days in',month,'is',31)
#     elif month == 'apr':
#         print('number of days in',month,'is',30)
#     elif month == 'may':
#         print('number of days in',month,'is',31)
#     elif month == 'jun':
#         print('number of days in',month,'is',30)
#     elif month == 'jul':
#         print('number of days in',month,'is',31)
#     elif month == 'aug':
#         print('number of days in',month,'is',31)
#     elif month == 'sep':
#         print('number of days in',month,'is',30)
#     elif month == 'oct':
#         print('number of days in',month,'is',31)
#     elif month == 'nov':
#         print('number of days in',month,'is',30)
#     elif month == 'dec':
#         print('number of days in',month,'is',31)

# num_days('oct')
# optimize/shorten the code in the function
# try to reduce the number of conditionals 

#* phase 1 
# def num_days(month):

#     if month == 'jan' or month == 'mar' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
#         print('number of days in',month,'is',31)
#     elif month == 'feb':
#         print('number of days in',month,'is',28)
#     elif month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
#         print('number of days in',month,'is',30)

# num_days('jul')

#* phase 2

def num_days(month):

    if month == 'jan' or month == 'mar' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
        print('number of days in',month,'is',31)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    else:
        print('number of days in',month,'is',30)

num_days('jun')

#? phase 3

# def num_days(month):
#     days = 31
#     if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
#         days = 30
#     elif month == 'feb':
#         days = 28
#     print('number of days in',month,'is',days)
    
# num_days('jun')

#? phase 4 

def num_days(month):
    days = 31
    if month in {'apr','jun','sep','nov'}:
    #if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in',month,'is',days)
    

num_days('jan')