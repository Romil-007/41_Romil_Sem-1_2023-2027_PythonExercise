# Write a Python program to create a class representing a stack data structure.
# Include methods for pushing and popping elements.

from multipledispatch import dispatch
    
    
class Stack:
    def __init__(self):
        self.l = []

    def push(self,ele):
        self.l.append(ele)
    
    def popping(self,ind=None):
        if(ind == None):
            self.l.pop()
        else:
            self.l.pop(ind)
        

    def getstack(self):
        return self.l



a = Stack()
a.push[1]
a.push[2]
a.push[3]

print(a.getstack())
    
