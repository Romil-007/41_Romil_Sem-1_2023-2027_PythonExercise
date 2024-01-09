class Car:
    def __init__ (self,make,model , year):
        self.make = make
        self.model = model
        self.year = year

    def showdata(self):
        print(f"Mfg - {self.make}\nModel - {self.model}\nYear - {self.year}")

make = input("Enter the manufacturing company : ")
model = input("Enter the name of model : ")
year = input("Enter the year of manufacture : ")
a = Car(make,model,year)
a.showdata()