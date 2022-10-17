
#* Properties - more 'pythonic'

class SoftwareEngineer:

    def __init__(self):
        self._salary = None

    # getter
    # def get_salary(self):
    #     return self._salary
    @property
    def salary(self):
        return self._salary
    
    # setter
    # def set_salary(self, value):
    #     self._salary = value
    @salary.setter
    def salary(self, value):
        self._salary = value
    
    #  deletes attribute - not common 
    # @salary.deleter
    # def salary(self):
    #     del self._salary

    
se = SoftwareEngineer()

se.salary = 6000
print(se.salary) # 6000