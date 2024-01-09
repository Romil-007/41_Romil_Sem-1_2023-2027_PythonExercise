class Employee:
    def __init__(self):
        print("Employee")
        self.id = 101

    
class Student:
    def __init__(self):
        print("Student")
        self.roll = 101
    

class Personinfo(Student,Employee):
    def __init__(self):
        super().__init__()
        Employee.__init__(self)

a = Personinfo()