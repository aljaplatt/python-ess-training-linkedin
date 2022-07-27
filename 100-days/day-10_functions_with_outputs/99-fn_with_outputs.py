from cgitb import reset


def my_function(num1, num2):
    result = num1 * num2
    return result

result_saved = my_function(6, 8)

# print(result_saved)

def format_name(first_name, last_name):
    converted = f'{first_name} {last_name}'.title()
    length = len(converted)
    return converted, length

# name = format_name('alex', 'PLATT')
# print(name) #? Alex Platt

fn_save = format_name('alex', 'platt')
print(fn_save[0]) #* Alex Platt
print(fn_save[1]) #* 10
print(type(fn_save))