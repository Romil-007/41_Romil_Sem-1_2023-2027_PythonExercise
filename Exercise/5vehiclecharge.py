class Vehicle:

    def __init__(self,seat):

        self.capacity = seat
        self.defaultfare = 100*self.capacity

    def showfare(self):
        return self.defaultfare
    
class Bus(Vehicle):

    def __init__(self,seat):

        super().__init__(seat)
        self.defaultfare += (0.1 * self.defaultfare)
    
    def showfare(self):
        
        return self.defaultfare
    
ask = int(input("Enter the type of vehicle\n1.Normal vehicle\n2.Bus"))
if(ask == 1):
    seat = int(input("Enter the seat in vehicle"))
    scooty = Vehicle(seat)
    print("Scooty fare : INR",scooty.showfare())
elif(ask == 2):
    seat = int(input("Enter the number of seat : "))
    mahindra = Bus(seat)
    print("Mahindra Bus fare : INR",mahindra.showfare())
else:
    print("Wrong Input Error")




