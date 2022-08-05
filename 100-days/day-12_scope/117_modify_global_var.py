# enemies = 1

# def inc_nmes():
#     global enemies
#     enemies += 1
#     # print()
# inc_nmes()

#* You can do the above but it is not advised to modify global scope scope like this

# def inc_nmes():
#     global enemies
#     enemies += 1
#     # print()
# inc_nmes()

# * Global constants OK - use UPPERCASE 

PI = 3.14
URL = 'google.com'

#What will be printed in the console when the following code is run?

def a_function(a_parameter):
    a_variable = 15
    return a_parameter
 
a_function(10)
print(a_variable) #? NameError It's trying to print a variable that is local to a_function() and is only available inside the function.


