fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as e:
        print(f"Error: {e}")
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(2)

# Traceback (most recent call last):
#   File "/Users/alexplatt/Desktop/projects/python-ess-training-linkedin/100-days/day-30_err_handling/ex1.py", line 9, in <module>
#     make_pie(4)
#   File "/Users/alexplatt/Desktop/projects/python-ess-training-linkedin/100-days/day-30_err_handling/ex1.py", line 5, in make_pie
#     fruit = fruits[index]
#             ~~~~~~^^^^^^^
# IndexError: list index out of range