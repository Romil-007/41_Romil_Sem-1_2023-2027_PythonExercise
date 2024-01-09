# Create a base class called “Vehicle” with a method called “drive.” Implement two
# subclasses, “Car” and “Bicycle,” that inherit from “Vehicle” and override the “drive”
# method with their own implementations.


class Vehicle:
    def __init__(self,name) :
        self.name = name
    def drive(self):
        print(f"{self.name} is the name of vehicle ")
class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    def drive(self):
        print(f"{self.name} is the name of car ")
class Bicycle(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    def drive(self):
        print(f"{self.name} is the name of Bicycle ")

ask = input("Enter the type\n1.General Vehicle\n2.Car\n3.Bicycle")
name = input("Enter the name : ")
if ask == "1":
    Veh = Vehicle(name)
elif ask == "2":
    Veh = Car(name)
else:
    Veh = Bicycle(name)

Veh.drive()



    
