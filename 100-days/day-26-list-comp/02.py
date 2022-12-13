
#? 1//  
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n * n for n in numbers]
# squared_numbers = [n** for n in numbers]

print(squared_numbers) # [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]

#? 2//  
# result = [n % 2 == 0 for n in numbers if n == True]
# result = [for n in numbers if n % 2 == 0]
#* we don't want to actually do anything to the num, just add it if it passes the if clause 
result = [num for num in numbers if num %2 == 0]

print(result) # [2, 8, 34]