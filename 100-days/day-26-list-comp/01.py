# without list comprehension

numbers = [1,2,3]

new_list = []

for n in numbers:
    add_one = n+1
    new_list.append(add_one)

print(new_list) # [2, 3, 4]

# with LC
# follow this pattern 

#* new_list = [new_item for item in list]
# new item is the expression, or action needed to get the new value 
# in this example we use line 8 - add_one = n + 1
list_comp_new_list = [n + 1 for n in numbers] 
print(list_comp_new_list) # [2, 3, 4]

names = ["Alex", "Kelly", "Alan", "Jen"]

xmas_names = [f"Merry christmas {name}" for name in names]
# ['Merry christmas Alex', 'Merry christmas Kelly', 'Merry christmas Alan', 'Merry christmas Jen']
print(xmas_names)

name = "Alexander"

letters_list = [letter for letter in name]
print(letters_list)
# ['A', 'l', 'e', 'x', 'a', 'n', 'd', 'e', 'r']

# nums_list = [num * 2 for num in range(1,5)]
# print(nums_list) # [2, 4, 6, 8]

#? Conditional list comprehension

#* new_list = [new_item for item in list if test]

nums_list = [num * 2 for num in range(1,10) if num > 4]
print("NL: ",nums_list) # NL:  [10, 12, 14, 16, 18]

sort_names = [name for name in names if len(name) < 4]
print(sort_names) # ['Jen']

long_names = [name.upper() for name in names if len(name) > 3]
print(long_names) # ['ALEX', 'KELLY', 'ALAN']