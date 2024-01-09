class Vehicle:
    def __init__(self,color,brand,type):
        self.color = color
        self.brand = brand
        self.type = type

    def showdata(self):
        print(f"A Vehicle of brand {self.brand} is {self.color}")
    
class SUV(Vehicle):
    def __init__ (self,color,brand):
        self.type = "SUV"
        Vehicle.__init__(self,color,brand,self.type)

    def showdata(self):
        print(f"A SUV VEHICLE OF {self.brand} is {self.color}")


a = SUV("White","Bmw")
a.showdata()
    