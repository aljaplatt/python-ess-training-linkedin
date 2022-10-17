
#* encapsulation is the mechanism of hiding data implementation, keeping instance variables private. 

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None #! single _
        self._num_bugs_solved = 0 
    
    #todo - this makes it unnecessary to access the bugs solved attribute from the outside. 
    def code(self):
        self._num_bugs_solved += 1

    def get_salary(self):
        return self._salary
    
    def set_salary(self, base_value):
        # check value, enforce constraints 
        self._salary = self._calc_salary(base_value)

    #* _calc_salary will never be called externally, only when set_salary is called 
    def _calc_salary(self, base_value ):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3 

se = SoftwareEngineer("Alex", 35)


# * se 'codes' 70 times = 70 bugs fixed 
for i in range(70):
    se.code()

# print(se._num_bugs_solved) # 70

# set base salary
se.set_salary(10000)

# get salary - 70 bugs means the 2* bonus should be applied
print(se.get_salary()) # 20000 - works 





