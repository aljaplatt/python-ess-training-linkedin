python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

#membership test
# print('arthur' in holy_grail)
print('Arthur' in holy_grail)

if 'Arthur' not in python:
    print('He\'s not here')


people = {}
people1 = {}
people2 = {}
#method 1 update
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
print(people)

#method 2 comprehension - same as above  
for groups in (python,holy_grail,life_of_brian) : people1.update(groups)
print(people1)

# only python holy grail 
for groups in (python,holy_grail) : people1.update(groups)


#method 3 unpacking 3.5 later
people2 = {**python,**holy_grail,**life_of_brian}
print(people2)
print(sorted(people2.items()))

print('The sum of the ages: ', sum(people.values()))