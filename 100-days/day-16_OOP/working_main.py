from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#* 1: print report - report is a method on the coffee maker class

#? This step creates a coffee_maker object from the class CoffeeMaker 
coffee_maker = CoffeeMaker()
# coffee_maker.report()
is_on = True

#? This step creates a money_machine object from the class MoneyMachine.
#? the construction occurs by adding the parenthesis - MoneyMachine()
money_machine = MoneyMachine()
# money_machine.report()

#* 2: check resources sufficient 
#? is_resources_sufficient requires a drink parameter. We can get this through the Menu Class.

#? The Menu class has 2 useful methods. 
#? ''' get_items() Returns all the names of the available menu items as a concatenated string. e.g. “latte/espresso/cappuccino” 
# 
#? - find_drink(order_name) Parameter order_name: (str) The name of the drinks order.  Searches the menu for a particular drink by name. Returns a MenuItem object if it exists, otherwise returns None. 
# 
#! We need both to ask the user what they want
# '''
menu = Menu()

while is_on:
    ''' This returns a string of all the drinks available '''
    options = menu.get_items()
    ''' We can get the users choice by asking them  '''
    choice = input(f'What would you like? ({options}): ')
    #way of quitting while loop 
    if choice == 'off':
        is_on = False 
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        #? find drink takes order names as input - choice 
        drink = menu.find_drink(choice)
        # print(drink) #? <menu.MenuItem object at 0x100abb910>
        # print(coffee_maker.is_resource_sufficient(drink))
        # if coffee_maker.is_resource_sufficient(drink):
        #* 3: Process coins 
            #? menu object has 3 attributes name, cost, ingredients
            # print(money_machine.make_payment(drink.cost))
            # if money_machine.make_payment(drink.cost): 
                # coffee_maker.make_coffee(drink)
        #* REFACTOR  
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



#? In the MoneyMachine class, we don't have a way to process the coins.
#?  money machine has a method called process coins that is called when make payment is triggered - 
#* 4: Check transaction successful - fulfilled at the same time as 3.
#* Make coffee    

