"""
class MW:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        self.__designation = "SCE" # Private attribute ->   Encapsulation

    def work(self):
        print( f"{self.name} works at MW")

    def get_des(self):
        return self.__designation

obj = MW("Leo",1209)
print(obj.name)
print(obj.work())
print(obj.get_des())    # Ouput: SCE

# if we try to print obj.__designation directly, it ll throw error
# print(obj.__designation)


class A:
    def feat1(self):
        print("A feature 1")

    def feat2(self):
        print("A feature 2")

class B(A):
    def feat3(self):
        print("B feature 3")

    def feat4(self):
        print("B feature 4")

obj = B()
obj.feat1()

class dog:
    def make_sound(self):
        return "bark"

class cat:
    def make_sound(self):
        return "meow"

def find_pet(pet):
    print(pet.make_sound())

d = dog()
find_pet(d)

c = cat()
find_pet(c)

"""

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Running")

#comp = Computer()
#comp.process()

comp1 = Laptop()