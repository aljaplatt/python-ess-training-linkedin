
with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

# result = [new_item for item in list if test]
# result = [num for num in file_1_data if num in file_2_data]
result = [int(num) for num in file_1_data if num in file_2_data]
# Write your code above 👆

# print(result) ['3\n', '6\n', '5\n', '33\n', '12\n', '7\n', '42\n', '13\n']
print(result) # [3, 6, 5, 33, 12, 7, 42, 13]

