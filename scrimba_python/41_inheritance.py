print("Class Inheritance")

# class Person:
#     def move(self):
#         print("Moves 4 paces")
#     def rest(self):
#         print("Gains 4 health points")
# class Doctor(Person):
#     pass
    
# character1=Person()
# character1.move()


class Person:
    def move(self):
        print("Moves 4 paces")
    def rest(self):
        print("Gains 4 health points")

class Doctor(Person):
    def heal(self):
        print("Heals 10 health points")

class Fighter(Person):
    def fight(self):
        print("Do 10 health points of damage")
    def move(self):
        print("Moves 6 paces")

class Wizard(Doctor, Fighter):
    def cast_spell(self):
        print("Turns invisble")
    def heal(self):
        print("Heals 15 health points")

    
character1=Doctor()
character1.move()
character1.heal()

character2=Fighter()
#! character2.heal() #* AttributeError: 'Fighter' object has no attribute 'heal'
character2.fight() #* ✅


character3=Wizard()
character3.heal()
character3.move() #? inherits from Doctor, who inherits from Person