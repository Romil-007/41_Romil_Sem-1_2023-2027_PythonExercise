# Define a class with a generator which can iterate the numbers, which are divisible
# by 7, between a given range 0 and n.

class function:
    def generator(self,n):
        l = []
        for i in range(7,n,7):
            l.append(i)
        return l
    
num = int(input("Enter the upper limit of 7 multiplication table : "))
a = function()
l= a.generator(num)
print(f"All the divisble number by 7 till {num} : ({len(l)})")
for i in l:
    print(i)


        