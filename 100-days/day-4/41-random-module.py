import random
import my_module

random_int = random.randint(1,10)
print(random_int)

print(my_module.special_numbers)

random_float = random.random() #* 0 -> 0.999999

#* Random float between 0 & 5 ?

random_float * 5 #* 0.0000... -> 4.99999....
