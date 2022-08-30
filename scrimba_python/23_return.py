# def value_added_tax(amount):
#     tax = amount * 0.25
    
# print(value_added_tax(100)) #? None

# def value_added_tax(amount):
#     tax = amount * 0.25
#     return tax
    
# print(value_added_tax(100)) #? 25.0

# def value_added_tax(amount):
#     tax = amount * 0.25
#     total_amount = amount * 1.25
#     return f"{amount}, {tax}, {total_amount}"
    
# price = value_added_tax(100)    
# print(price, type(price))

def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return [amount, tax, total_amount]
    
price = value_added_tax(100)    
print(price[1], type(price))