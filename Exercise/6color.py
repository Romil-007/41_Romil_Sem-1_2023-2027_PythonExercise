class Vehicle:
    def __init__ (self,nme,clr = "White"):
        self.name = nme
        self.color = clr
    
    def showdata(self):
        print(f"{self.name} is {self.color}")


a = Vehicle("Porsche" , "Black")
b = Vehicle("Mercedes")

a.showdata()
b.showdata()