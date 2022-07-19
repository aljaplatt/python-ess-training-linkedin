
#* range
#? print even nums between 1 -10
# for number in range(1, 11):
#     if number % 2 == 0:
#         print(number)


#* you can add a step count param
# 1,6,11,16
# for num in range(1,21, 5):
#     print(num) 
#* 0 5 10 15 20
# arr = []
# for num in range(0,21, 5):
#     print(num) 
#     arr.append(num)
# print(arr)

# total = 0   
# for num in range(1, 101):
#     total += num

total = 0   
for num in range(1,101):
    if num % 2 == 0:
        total += num
        
print(total)

totes = 0
for num in range(2, 101, 2):
    totes += num

print(totes)
