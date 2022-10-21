
#? getters and setters encapsulate data from the outside world 
#* Unlike in Java, where class variables are private and must be accessed through getters and setters, in python there is no need to do this immediately everything is public. Python favours the uniform access principle - https://en.wikipedia.org/wiki/Uniform_access_principle

from _13class_methods import MercedesBenz, m1

#? we can just do this to amend the class attribute
m1.doors += 1 
print(m1.doors) # 5

#* The default is to have all attributes be publicly accessible 

#* It is possible to implement this behaviour through the use of properties, which allow the same syntax to access and set data. 