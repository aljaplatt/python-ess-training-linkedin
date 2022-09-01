python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

#membership test
# print('arthur' in holy_grail) #? False
print('Arthur' in holy_grail) #? True

if 'Arthur' not in python:
    print('He\'s not here')

#* Combining dictionaries  

people = {}
people1 = {}
people2 = {}

#method 1 update - take a dictionary and add another one to it.
people.update(python)
# people is now a 'clone' of the python dictionary
 
people.update(holy_grail)
people.update(life_of_brian)
print(people)

#method 2 comprehension - same as above  
for groups in (python,holy_grail,life_of_brian) : people1.update(groups)
print(people1)

# only python holy grail 
for groups in (python,holy_grail) : people1.update(groups)


#method 3 unpacking 3.5 later - same, but not sorted in the same way
people2 = {**python,**holy_grail,**life_of_brian}
print(people2)

# so this will sort them
print(sorted(people2.items()))

print('The sum of the ages: ', sum(people.values()))