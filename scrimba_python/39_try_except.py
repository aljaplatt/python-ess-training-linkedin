print("Errors: Try/Except")

#try:
    #code you want to run
#except:
    #executed if error occurs
#else:
    #executed if no error
#finally:
    #always executed 

#* 1 
try:
    num=int(input('Enter a number: '))
    print("30 divided by",num, "is: ", 30/num)
except:
    print("Invalid Input!")
print("**Thank you for playing!**")

#* 2
# try:
#     num=int(input('Enter a number: '))
#     print("30 divided by",num, "is: ", 30/num)
# except ZeroDivisionError:
#     print("You can't divide by Zero!!!")
# except ValueError:
#     print("Bad Value!")
# except:
#     print("Invalid Input!")
# print("**Thank you for playing!**")

#* 3

# try:
#     num=int(input('Enter a number: '))
#     print("30 divided by",num, "is: ", 30/num)
# except ZeroDivisionError as err:
#     print(err, "You can't divide by Zero!!!")
# except ValueError as err:
#     print(err, "Bad Value!")
# except:
#     print("Invalid Input!")
# print("**Thank you for playing!**") 

#* 4

# try:
#     num=int(input('Enter a number: '))
#     num1 = 30/num
# except ZeroDivisionError as err:
#     print(err, "You can't divide by Zero!!!")
# except ValueError as err:
#     print(err, "Bad Value!")
# except:
#     print("Invalid Input!")
# else:
#     print("30 divided by",num, "is: ", 30/num)
# finally:
#     print("**Thank you for playing!**")

#* 5

# try:
#     num=int(input('Enter a number between 1 and 30: '))
#     num1 = 30/num
#     if num > 30:
#         raise ValueError(num)
# except ZeroDivisionError as err:
#     print(err, "You can't divide by Zero!!!")
# except ValueError as err:
#     print(err,num, "Bad Value not between 1 and 30!")
# except:
#     print("Invalid Input!")
# else:
#     print("30 divided by",num, "is: ", 30/num)
# finally:
#     print("**Thank you for playing!**")
