
class Dog:

    # method = function inside class
    def bark(self):
        print("Bark")

    def add_one(self, x):
        return x + 1


d = Dog()

d.bark()
print(d.add_one(50))