
# is_raining = True
# is_cold = True
# print("Good Morning")
# if is_raining or is_cold:
#     print("Bring Umbrella")
# else:
#     print("Umbrella is optional")

# is_raining = True
# is_cold = True
# print("Good Morning")
# if is_raining and is_cold:
#     print("Bring Umbrella and jacket")
# else:
#     print("Umbrella is optional")

is_raining = True
is_cold = True
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and jacket")
elif is_raining and not(is_cold):
    print("Bring Umbrella")
elif not(is_raining) and is_cold:
    print("Bring Jacket")
else:
    print("Umbrella is optional")