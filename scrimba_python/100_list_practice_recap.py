# friends = ['John','Michael','Terry','Eric','Graham']
# # cars = [911,130,328,535,740,308]
# print(friends) #? - ['John', 'Michael', 'Terry', 'Eric', 'Graham']
# friends.sort() #? - ['Eric', 'Graham', 'John', 'Michael', 'Terry'] - alphabetically
# print(friends)
# # friends.sort(reverse=True)
# # print(friends) #? - ['Terry', 'Michael', 'John', 'Graham', 'Eric'] reverses state
# friends.reverse()
# print(friends)  #? - ['Terry', 'Michael', 'John', 'Graham', 'Eric'] reverses state


sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]

last_sale = int(input('Add a number: '))
sales_w2.append(last_sale)

# sales.extend(sales_w1) etc
sales = sales_w1 + sales_w2
print(sales)

# best_day = max(sales)
# worst_day = min(sales)
# print(best_day,':',worst_day)

sales.sort()
print(sales)
bad = sales[0] * 1.5
good = sales[-1] * 1.5