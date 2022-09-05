# def func(n):
#     return n
    
# print(func(3))
# print(type(func(3))) #? return value is an int - <class 'int'>

def func(n):
    return lambda a: a*n
    
print(type(func(3))) #* using a lambda, the return value is a function - <class 'function'>


def func(n):
    return lambda a: a*n
# a*2
doubler = func(2)
print('doubler: ',doubler(3))

quintipler = func(5)
print('quintipler: ',quintipler(3))

# n is the func num, a is the num used when calling function 
decimator = func(10)
# decimator - is the lambda returned from func()
print('decimator: ', decimator(2))


def price_calc(start,hourly_rate):
    return lambda hours: start + hourly_rate * hours
    
# walkin_cost = price_calc(10,30)
# print(walkin_cost(2)) # 70

# premium_cost = price_calc(1,25)
# print(premium_cost(2)) # 51
# print(price_calc(1,25)(2))


# print((lambda a,b,c: a+b+c)(2,3,4)) #? 9 
# print((lambda a,b,c=2: a+b+c)(2,3))
# print((lambda a,b,c=2: a+b+c)(2,c=3,b=4))
# print((lambda *args: sum(args))(2,3,4, 50))