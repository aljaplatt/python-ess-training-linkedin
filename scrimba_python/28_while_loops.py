# print("1.*Loops are great*")
# print("2.**Loops are great**")
# print("3.***Loops are great***")
# print("4.****Loops are great****")
# print("5.*****Loops are great*****")

count = 10
num = 0
stars = ''
while count:
    num += 1
    stars += '*'
    print(f'{num}.{stars}Loops are great{stars}')
    count -= 1