from datetime import date 

class Person:
    def __init__(self , name , dob , country):
        self.name = name
        self.dob = dob
        self.country = country
    
    def calcage(self):
        age = 0
        today = str(date.today()).split("-")
        age = (int(today[0]) - int(self.dob[2]) - 1)
        if(int(today[1])>=int(self.dob[1])):
            if(int(today[1]) == int(self.dob[1])):
                if(int(today[2]) >= int(self.dob[0])):
                    age += 1
            else:
                age += 1

        return age

        


name = input("Enter person's name : ")
dob = input("Enter dob (dd-mm-yyyy):  ").split("-")
country = input("Enter the country : ")

obj = Person(name,dob,country)

print(f"Name : {name} \nAge : {obj.calcage()} \nCountry : {country}")