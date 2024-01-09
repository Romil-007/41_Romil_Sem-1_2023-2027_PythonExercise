class Animal:
    def __init__ (self):
        self.legs = 4
        self.kingdom = "Mammal"
    
    def method(self):
        print(f"This is a part of Animal ")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.favfood = "Pedigree"
    
    def method(self):
        print(f"Animal Type : Dog\nFav Food : {self.favfood}") 

class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.favfood = "Cat nip"
    
    def method(self):
        print(f"Animal Type : Cat\nFav Food : {self.favfood}") 

a = Dog()
b = Cat()
a.method()
b.method()
c = Animal()
c.method()